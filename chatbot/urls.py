from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', include('botuser.urls')),
    #path('slack/', include('django_slack_oauth.urls')),
]