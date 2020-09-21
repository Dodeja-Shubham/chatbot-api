import os
import datetime
from chatbot import settings
from slack import WebClient
from slack.errors import SlackApiError
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response

from .serializers import Send_Message_Serializer, Schedule_Message_Serializer
from .models import Send_Message, Schedule_Message

class Send_Message_View(generics.GenericAPIView,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,):

    serializer_class = Send_Message_Serializer
    queryset = Send_Message.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        '''
        GET Request
        '''
        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
    
    @csrf_exempt
    def post(self, request):
        '''
        Create Request
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data.get('is_user') == True:
                client = WebClient(token= settings.OAUTH_ACCESS_TOKEN)
            else:
                client = WebClient(token= settings.BOT_USER_ACCESS_TOKEN)
            try:
                response = client.chat_postMessage(
                    channel=serializer.validated_data.get('channel'),
                    text=serializer.validated_data.get('text'),
                    )
                assert response["message"]["text"] == serializer.validated_data.get('text')
                serializer.save()
                return Response(status=status.HTTP_200_OK)
            except SlackApiError as e:
                assert e.response["ok"] is False
                assert e.response["error"]
                return Response(f"Got an error: {e.response['error']}", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Schedule_Message_View(generics.GenericAPIView,
                    mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.RetrieveModelMixin,):

    serializer_class = Schedule_Message_Serializer
    queryset = Schedule_Message.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):
        '''
        GET Request
        '''

        if id:
            return self.retrieve(request,id)
        else:
            return self.list(request)
            
    @csrf_exempt
    def post(self, request):
        '''
        Create Request
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            send_at = serializer.validated_data.get('post_at')
            year = send_at.year
            month = send_at.month
            date = send_at.day
            hour = send_at.hour
            minute = send_at.minute
            epoch_time = datetime.datetime(year,month,date,hour,minute).timestamp()
            if serializer.validated_data.get('is_user') == True:
                client = WebClient(token= settings.OAUTH_ACCESS_TOKEN)
            else:
                client = WebClient(token= settings.BOT_USER_ACCESS_TOKEN)
            try:
                response = client.chat_scheduleMessage(
                    channel=serializer.validated_data.get('channel'),
                    text=serializer.validated_data.get('text'),
                    post_at= epoch_time
                    )
                assert response["message"]["text"] == serializer.validated_data.get('text')
                serializer.save()
                return Response(f"Scheduled Message ID: {response['scheduled_message_id']}", status=status.HTTP_200_OK)
            except SlackApiError as e:
                assert e.response["ok"] is False
                assert e.response["error"]
                return Response(f"Got an error: {e.response['error']}", status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

