from django.urls import include, path
from botuser import views
urlpatterns = [
    path('send/', views.Send_Message_View.as_view()),
    path('schedule/', views.Schedule_Message_View.as_view(), name='schedule'),
    path('conversation', views.Join_Conversation_View.as_view(), name='conversation-list'),
    path('conversation/list', views.List_Conversation_View.as_view(), name='conversation-list')
]