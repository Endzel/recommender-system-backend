import uuid

from django.conf import settings
from django.db import models
from django.dispatch import receiver

from recommender.models import PertenanceGrade, Antecedent, Consequent, UserContext, RecommendationContext, Recommendation, Item, Group
from recommender.utils import RequestUtils, add_query_params

from rest_framework.authtoken.models import Token


# Create user token automatically
@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# Set group title
@receiver(models.signals.pre_save, sender=Group)
def generate_default_group_name(sender, instance, created=False, **kwargs):
    if created and not instance.title:
        instance.title = uuid.uuid4().hex


# Create or update an attribute-value pair
@receiver(models.signals.post_save, sender=PertenanceGrade)
def create_or_update_attribute_pertenance_pair(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveItem?'
    params = {
        "attribute": instance.item_attribute.name,
        "itemsset": instance.item.city.name,
        "name": instance.item.name,
        "system": "tfgangel",
        "value": instance.value,
    }

    url_params = add_query_params(url, params)

    RequestUtils.postRequest(url_params, {})


# Create or update an Antecedent
@receiver(models.signals.post_save, sender=Antecedent)
def create_or_update_antecedent(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveRule?'
    params = {
        "attribute": instance.item_attribute.name,
        "part": 'a',
        "ruledesc": 'Antecedente de ' + instance.implication.context_segment.domain + ' para ' + instance.item_attribute.name,
        'rulesset': instance.implication.context_segment.dimension,
        "system": "tfgangel",
        "value": instance.value,
    }

    url_params = add_query_params(url, params)

    RequestUtils.postRequest(url_params, {})


# Create or update a Consequent
@receiver(models.signals.post_save, sender=Consequent)
def create_or_update_consequent(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveRule?'
    params = {
        "attribute": instance.item_attribute.name,
        "part": 'c',
        "ruledesc": 'Consecuente de ' + instance.implication.context_segment.domain + ' para ' + instance.item_attribute.name,
        'rulesset': instance.implication.context_segment.dimension,
        "system": "tfgangel",
        "value": instance.value,
    }

    url_params = add_query_params(url, params)

    RequestUtils.postRequest(url_params, {})


# Create or update a profile attribute
@receiver(models.signals.post_save, sender=UserContext)
def create_or_update_profile_attribute(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveProfile?'
    params = {
        "profileattribute": instance.context_segment.domain,
        "ruledesc": 'Contexto de usuario de tipo ' + instance.context_segment.domain,
        'userdesc': instance.user.first_name + ' ' + instance.user.last_name,
        "system": "tfgangel",
        "value": instance.weight,
    }

    url_params = add_query_params(url, params)

    RequestUtils.postRequest(url_params, {})


# Create or update a profile attribute for recommendation
@receiver(models.signals.pre_save, sender=Recommendation)
def create_or_update_recommendation_profile_attribute(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveProfile?'
    url_params = {
        "profileattribute": instance.context.context_segment.domain,
        "ruledesc": 'Contexto de grupo de tipo ' + instance.context.context_segment.domain,
        'userdesc': instance.group.title,
        "system": "tfgangel",
        "value": instance.context.weight,
    }

    url_params = add_query_params(url, url_params)

    RequestUtils.postRequest(url_params, {})


# Get recommendations for a group in a context and with rules set
@receiver(models.signals.post_save, sender=Recommendation)
def generate_recommendation(sender, instance, created=False, **kwargs):

    url = settings.RECOMMENDER_API + 'recommender/getRecommendations?'
    params = {
        "itemsset": instance.city,
        'rulesset': instance.context.context_segment.dimension,
        'userdesc': instance.group.title,
        "system": "tfgangel",
    }

    url_params = add_query_params(url, params)

    result = RequestUtils.getRequest(url_params)
    result_json = result.json()

    if result_json:
        for item in result_json:
            i = Item.objects.filter(name__iexact=item['name'])
            if i.exists():
                instance.items.add(i.last().pk)
