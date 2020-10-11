# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import SlackAuthView, DefaultSuccessView, GetTokens


urlpatterns = [
    url('login/', SlackAuthView.as_view(), name='slack_auth'),
    url('success/', DefaultSuccessView.as_view(), name='slack_success'),
    url('token/', GetTokens.as_view(), name="Tokens")
]
