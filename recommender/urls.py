from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from recommender.endpoints.user import UserView, LoginView, LogoutView, RegisterView, ForgotPasswordView, ChangePasswordView, UserChoicesView
from recommender.endpoints.group import GroupView, GroupSingleView
from recommender.endpoints.item import ItemView, ItemSingleView, ItemValoratedView, ItemAttributeView, AttributeCategoryView, CityView, CityChoicesView, PertenanceGradeView
from recommender.endpoints.recommendation import RecommendationView, RecommendationSingleView, RecommendationValoratedView
from recommender.endpoints.context import ContextSegmentView, UserContextView, UserContextSingleView, RecommendationContextView, ImplicationView, ContextSegmentChoicesView
from recommender.endpoints.valoration import ValorationView, ValorationSingleView


api_urls = [
    # User
    url(r'^users$', UserView.as_view(), name='userFrontView'),
    url(r'^users/login$', csrf_exempt(LoginView.as_view()), name='loginFrontView'),
    url(r'^users/logout$', LogoutView.as_view(), name='logoutFrontView'),
    url(r'^users/register$', RegisterView.as_view(), name='registerFrontView'),
    url(r'^users/forgot_password$', ForgotPasswordView.as_view(), name='forgotPasswordFrontView'),
    url(r'^users/change_password$', ChangePasswordView.as_view(), name='changePasswordFrontView'),

    # Group
    url(r'^groups$', GroupView.as_view(), name='groupFrontView'),
    url(r'^groups/(?P<pk>.+)$', GroupSingleView.as_view(), name='groupSingleFrontView'),

    # Item
    url(r'^items$', ItemView.as_view(), name='itemFrontView'),
    url(r'^items/valorated$', ItemValoratedView.as_view(), name='itemValoratedFrontView'),
    url(r'^items/(?P<pk>.+)$', ItemSingleView.as_view(), name='itemSingleFrontView'),
    url(r'^item_attributes$', ItemAttributeView.as_view(), name='itemAttributeFrontView'),
    url(r'^attribute_categories$', AttributeCategoryView.as_view(), name='attributeCategoryFrontView'),
    url(r'^pertenance_grades$', PertenanceGradeView.as_view(), name='pertenanceGradeFrontView'),
    url(r'^cities$', CityView.as_view(), name='cityFrontView'),

    # Recommendation
    url(r'^recommendations$', RecommendationView.as_view(), name='recommendationFrontView'),
    url(r'^recommendations/valorated$', RecommendationValoratedView.as_view(), name='RecommendationValoratedFrontView'),
    url(r'^recommendations/(?P<pk>.+)$', RecommendationSingleView.as_view(), name='recommendationFrontView'),

    # Context
    url(r'^context_segments$', ContextSegmentView.as_view(), name='contextSegmentFrontView'),
    url(r'^user_contexts$', UserContextView.as_view(), name='userContextFrontView'),
    url(r'^user_contexts/(?P<pk>.+)$', UserContextSingleView.as_view(), name='userContextSingleFrontView'),
    url(r'^recommendation_contexts$', RecommendationContextView.as_view(), name='recommendationContextFrontView'),
    url(r'^implications$', ImplicationView.as_view(), name='implicationFrontView'),

    # Valoration
    url(r'^valorations$', ValorationView.as_view(), name='valorationFrontView'),
    url(r'^valorations/(?P<pk>.+)$', ValorationSingleView.as_view(), name='valorationSingleFrontView'),

    # Choices
    url(r'^users/choices$', UserChoicesView.as_view(), name='userChoicesFrontView'),
    url(r'^cities/choices$', CityChoicesView.as_view(), name='cityChoicesFrontView'),
    url(r'^context_segments/choices$', ContextSegmentChoicesView.as_view(), name='contextSegmentChoicesFrontView'),
]
