import random
import string

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

from recommender import choices


def item_upload_to(instance, filename):
    return 'images/' + instance.city.name + '/' + filename


class CustomUserManager(BaseUserManager):
    def create(self, email, password, **extra_fields):
        return self.create_user(email, password, **extra_fields)

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('You should include an email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Super users must have is_staff flag activated')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Super users must have is_superuser flag activated')
        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    first_name = models.CharField(null=True, blank=True, max_length=140, verbose_name='First name')
    last_name = models.CharField(null=True, blank=True, max_length=140, verbose_name='Last name')
    email = models.EmailField(unique=True, verbose_name='Email')
    birth_date = models.DateField(null=True, blank=True, verbose_name='Birth date')
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    __change_password_token = None

    # Relations
    preferences = models.ManyToManyField('ItemAttribute', through="PreferenceGrade", verbose_name='Preferences')
    context_segments = models.ManyToManyField('ContextSegment', through="UserContext", verbose_name='Context segments')

    def __str__(self):
        return self.email

    def set_change_password_token(self):
        __change_password_token = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(32))
        return __change_password_token

    def change_password(self, token, password):
        if self.__change_password_token and token == self.__change_password_token:
            self.password = password
            self.__change_password_token = None
            self.save()
            return True
        return False

    def clear_change_password_token(self):
        __change_password_token = None

    def get_full_name(self):
        return self.first_name + ' ' + self.last_name


class PreferenceGrade(models.Model):

    value = models.IntegerField(default=0, verbose_name='Value')

    # Relations
    item_attribute = models.ForeignKey('ItemAttribute', on_delete=models.CASCADE, related_name='preference_grades', verbose_name='Item attribute')
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='preference_grades', verbose_name='User')

    def __str__(self):
        return str(self.id)


class UserContext(models.Model):

    weight = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name='Weight')

    # Relations
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='user_contexts', verbose_name='User')
    context_segment = models.ForeignKey('ContextSegment', on_delete=models.CASCADE, related_name='user_contexts', verbose_name='Context segment')

    def __str__(self):
        return str(self.id)


class Item(models.Model):

    name = models.CharField(blank=True, max_length=140, verbose_name='Name')
    description = models.TextField(blank=True, max_length=1000, verbose_name='Description')
    date = models.DateTimeField(null=True, blank=True, verbose_name='Date')
    image = models.ImageField(null=True, blank=True, upload_to=item_upload_to, verbose_name='Item image')
    gps_point = models.CharField(blank=True, max_length=140, verbose_name='GPS Point')
    weblink = models.URLField(blank=True, max_length=140, verbose_name='Web link')
    price = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name='Price')

    # Relations
    attributes = models.ManyToManyField('ItemAttribute', through="PertenanceGrade", verbose_name='Attributes')
    city = models.ForeignKey('City', null=True, on_delete=models.SET_NULL, related_name='items', verbose_name='City')

    def __str__(self):
        return self.name


class City(models.Model):

    name = models.CharField(blank=True, max_length=140, verbose_name='Name')
    country = models.TextField(blank=True, max_length=1000, verbose_name='Country')

    def __str__(self):
        return self.name


class PertenanceGrade(models.Model):

    value = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name='Value')

    # Relations
    item_attribute = models.ForeignKey('ItemAttribute', on_delete=models.CASCADE, related_name='pertenance_grades', verbose_name='Item attribute')
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name='pertenance_grades', verbose_name='Item')

    def __str__(self):
        return str(self.id)


class ItemAttribute(models.Model):

    name = models.CharField(blank=True, max_length=140, verbose_name='Name')

    # Relations
    category = models.ForeignKey('AttributeCategory', null=True, on_delete=models.SET_NULL, related_name='item_attributes', verbose_name='Item category')

    def __str__(self):
        return self.name


class AttributeCategory(models.Model):

    name = models.CharField(blank=True, max_length=140, verbose_name='Name')

    def __str__(self):
        return self.name


class Group(models.Model):

    title = models.CharField(blank=True, max_length=140, verbose_name='Title')
    description = models.TextField(blank=True, max_length=1000, verbose_name='Description')

    # Relations
    users = models.ManyToManyField('CustomUser', blank=True, verbose_name='Users')

    def __str__(self):
        return self.title or str(self.id)


class Recommendation(models.Model):

    # Relations
    items = models.ManyToManyField('Item', blank=True, verbose_name='Items')
    context_segments = models.ManyToManyField('ContextSegment', verbose_name='Context segments')
    group = models.ForeignKey('Group', on_delete=models.CASCADE, related_name='recommendations', verbose_name='Group')

    def __str__(self):
        return str(self.id)


class Valoration(models.Model):

    comment = models.TextField(blank=True, max_length=1000, verbose_name='Comment')
    score = models.IntegerField(default=0, verbose_name='Score')

    # Relations
    user = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='valorations', verbose_name='User')
    item = models.ForeignKey('Item', null=True, on_delete=models.CASCADE, related_name='valorations', verbose_name='Valorated item')
    recommendation = models.ForeignKey('Recommendation', null=True, on_delete=models.CASCADE, related_name='valorations', verbose_name='Recommendation')

    def __str__(self):
        return str(self.id)


class ContextSegment(models.Model):

    dimension = models.CharField(blank=True, max_length=140, verbose_name='Dimension')
    domain = models.CharField(blank=True, max_length=140, verbose_name='Domain')

    def __str__(self):
        return str(self.id)


class Implication(models.Model):

    # Relations
    antecedents = models.ManyToManyField('ItemAttribute', blank=True, through="Antecedent", related_name='implication_antecedents', verbose_name='Antecedents')
    consequents = models.ManyToManyField('ItemAttribute', blank=True, through="Consequent", related_name='implication_consequents', verbose_name='Consequents')
    context_segment = models.ForeignKey('ContextSegment', on_delete=models.CASCADE, related_name='implications', verbose_name='Context segment')

    def __str__(self):
        return str(self.id)


class Antecedent(models.Model):

    value = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name='Value')

    # Relations
    item_attribute = models.ForeignKey('ItemAttribute', null=True, on_delete=models.CASCADE, related_name='antecedents_values', verbose_name='Item attribute')
    implication = models.ForeignKey('Implication', null=True, on_delete=models.CASCADE, related_name='antecedents_values', verbose_name='Implication')

    def __str__(self):
        return str(self.id)


class Consequent(models.Model):

    value = models.DecimalField(null=True, max_digits=10, decimal_places=2, verbose_name='Value')

    # Relations
    item_attribute = models.ForeignKey('ItemAttribute', null=True, on_delete=models.CASCADE, related_name='consequents_values', verbose_name='Item attribute')
    implication = models.ForeignKey('Implication', null=True, on_delete=models.CASCADE, related_name='consequents_values', verbose_name='Implication')

    def __str__(self):
        return str(self.id)
