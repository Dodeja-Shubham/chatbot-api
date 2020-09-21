from rest_framework import serializers
from .models import Send_Message, Schedule_Message

class Send_Message_Serializer(serializers.ModelSerializer):
    # channel = serializers.CharField(max_length=100)
    # text = serializers.CharField(style={'base_template': 'textarea.html'})
    class Meta():
        model = Send_Message
        fields = '__all__'

class Schedule_Message_Serializer(serializers.ModelSerializer):
    class Meta():
        model = Schedule_Message
        fields = '__all__'