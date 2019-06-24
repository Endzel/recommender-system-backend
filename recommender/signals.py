from django.conf import settings
from django.db import models
from django.dispatch import receiver

from recommender.models import *
from recommender.utils import RequestUtils, add_query_params

from rest_framework.authtoken.models import Token


# Create user token automatically
@receiver(models.signals.post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


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

    response = RequestUtils.postRequest(url_params, {})


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

    response = RequestUtils.postRequest(url_params, {})


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

    response = RequestUtils.postRequest(url_params, {})


# Create or update a profile attribute
@receiver(models.signals.post_save, sender=UserContext)
def create_or_update_consequent(sender, instance, created=False, **kwargs):
    url = settings.RECOMMENDER_API + 'recommender/saveProfile?'
    params = {
        "profileattribute": instance.context_segment.domain,
        "ruledesc": 'Contexto de usuario de ' + instance.user.first_name + ' ' + instance.user.last_name + ' para ' + instance.context_segment.domain,
        'rulesset': instance.implication.context_segment.dimension,
        "system": "tfgangel",
        "value": instance.weight,
    }

    url_params = add_query_params(url, params)

    response = RequestUtils.postRequest(url_params, {})
