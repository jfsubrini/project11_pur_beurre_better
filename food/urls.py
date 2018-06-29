"""Food app URL Configuration."""


# Django imports
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    # PasswordChangeView,
    # PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
    )

# Import from my app
from . import views



urlpatterns = [
    #### Homepage
    path('', TemplateView.as_view(template_name='food/home.html'), name='home'),
    path('index/', TemplateView.as_view(template_name='food/home.html'), name='home'),
    path('home/', TemplateView.as_view(template_name='food/home.html'), name='home'),
    #### Account
    path('account/', views.account, name='account'),
    path('account/register/', views.register, name='register'),
    path('account/signin/', LoginView.as_view(
        template_name='food/account/signin.html'), name='signin'),
    path('account/signout/', LogoutView.as_view(template_name='food/home.html'), name='signout'),
    #### Password reset
    # path('account/password_change/', PasswordChangeView.as_view(
    #     template_name='food/account/password_change.html'), name='password_change'),
    # path('account/password_change/done/', PasswordChangeDoneView.as_view(
    #     template_name='food/account/password_change_done.html'), name='password_change_done'),
    path('account/password_reset/', PasswordResetView.as_view(
        template_name='food/account/password_reset.html'), name='password_reset'),
    path('account/password_reset_done/', PasswordResetDoneView.as_view(
        template_name='food/account/password_reset_done.html'), name='password_reset_done'),
    re_path(
        r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', \
        PasswordResetConfirmView.as_view(
            template_name='food/account/password_reset_confirm.html'), \
            name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='food/account/password_reset_complete.html'), name='password_reset_complete'),
    #### Results and information pages
    path('foodresult/', views.foodresult, name='foodresult'),
    path('foodinfo/<int:pk>/', views.FoodInfo.as_view(), name='foodinfo'),
    path('selection/', views.selection, name='selection'),
    path('imprint/', TemplateView.as_view(template_name='food/imprint.html'), name='imprint'),
    path('categories/', views.display_per_category, name='categories'),
]
