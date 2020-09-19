import os
from slack import WebClient
from slack.errors import SlackApiError
from django.views.generic import TemplateView

    

class Send_Message(TemplateView):
    template_name = "about.html"
    client = WebClient(
        token='xoxb-1374653515218-1368072411398-0aEaXgUzLh8lrCMWa6dNRGHB')
    try:
        response = client.chat_postMessage(
            channel='#random',
            text="Hello world!")
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        # You will get a SlackApiError if "ok" is False
        assert e.response["ok"] is False
        # str like 'invalid_auth', 'channel_not_found'
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")
