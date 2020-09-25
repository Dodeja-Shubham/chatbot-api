from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

#Restframewok imports
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Chatbot API",
      default_version='v1',
      description="This is the REST API documentation for Chatbot API\'s",
      terms_of_service="https://www.google.com/policies/terms/",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('botuser.urls')),
    path('slack/', include('django_slack_oauth.urls')),
    path('swagger/', schema_view.with_ui('swagger',
                                            cache_timeout=0), name='schema-swagger-ui')
]