from django.urls import include, path
from . import views
urlpatterns = [
    path('send/', views.Send_Message.as_view(), name='event_hook'),
]