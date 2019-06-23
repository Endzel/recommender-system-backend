from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from recommender.endpoints.user import UserView, LoginView, LogoutView, RegisterView, ForgotPasswordView, RecoverPasswordView, ChangePasswordView, UserChoicesView
from recommender.endpoints.group import GroupView
from recommender.endpoints.item import ItemView, ItemAttributeView, AttributeCategoryView, CityView, CityChoicesView
from recommender.endpoints.recommendation import RecommendationView
from recommender.endpoints.context import ContextSegmentView, ImplicationView, ContextSegmentChoicesView
from recommender.endpoints.valoration import ValorationView


api_urls = [
    # User
    url(r'^users$', UserView.as_view(), name='userFrontView'),
    url(r'^users/login$', csrf_exempt(LoginView.as_view()), name='loginFrontView'),
    url(r'^users/logout$', LogoutView.as_view(), name='logoutFrontView'),
    url(r'^users/register$', RegisterView.as_view(), name='registerFrontView'),
    url(r'^users/forgot_password$', ForgotPasswordView.as_view(), name='forgotPasswordFrontView'),
    url(r'^users/recover_password$', RecoverPasswordView.as_view(), name='recoverPasswordFrontView'),
    url(r'^users/change_password$', ChangePasswordView.as_view(), name='changePasswordFrontView'),

    # Group
    url(r'^groups$', GroupView.as_view(), name='groupFrontView'),

    # Item
    url(r'^items$', ItemView.as_view(), name='itemFrontView'),
    url(r'^item_attributes$', ItemAttributeView.as_view(), name='itemAttributeFrontView'),
    url(r'^attribute_categories$', AttributeCategoryView.as_view(), name='attributeCategoryFrontView'),
    url(r'^cities$', CityView.as_view(), name='cityFrontView'),

    # Recommendation
    url(r'^recommendations$', RecommendationView.as_view(), name='recommendationFrontView'),

    # Context
    url(r'^context_segments$', ContextSegmentView.as_view(), name='contextSegmentFrontView'),
    url(r'^implications$', ImplicationView.as_view(), name='implicationFrontView'),

    # Valoration
    url(r'^valorations$', ValorationView.as_view(), name='valorationFrontView'),

    # Choices
    url(r'^users/choices$', UserChoicesView.as_view(), name='userChoicesFrontView'),
    url(r'^cities/choices$', CityChoicesView.as_view(), name='cityChoicesFrontView'),
    url(r'^context_segments/choices$', ContextSegmentChoicesView.as_view(), name='contextSegmentChoicesFrontView'),
]
