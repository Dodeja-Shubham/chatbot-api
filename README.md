# chatbot-api

## Build

###### Virtual Enviornment activation
- `sudo apt install python3-venv`
- `python3 -m venv name_of_virtual_environment`
- `source name_of_virtual_environment/bin/activate`
###### Setting up project (Install requirements)
- `Pip install -r requirements.txt`
###### Create super user for admin
- `python manage.py createsuperuser` 
###### Execute the project
- `python manage.py runserver `




## Change Database Character-set to utf-8 for globalization
- `ALTER TABLE table_name CONVERT TO CHARACTER SET utf8;`

## API Documentation
- `API Documentation is mentained through Swagger Ui and can be access from the link below`
        [API documentation](https://chatbotmckinley.herokuapp.com/swagger)

## Resources

- [Django documentation](https://www.djangoproject.com/)
- [PostgreSQL Adapter](https://pypi.org/project/psycopg2/)
- [Slack API Documentation](https://api.slack.com/methods)
- [Django-Slack](https://django-slack.readthedocs.io/)

## Workflow
- Once the project is deployed onto a server below mentioned methods can be called from specific URLs
- [Send Message](https://chatbotmckinley.herokuapp.com/bot/send)
    `The Send Message method gives user 2 functionalities`
    1) Send Message as a bot (Set is_user = False)
    2) Send Message as a user (Set is_user = True) 
- [Schedule Message](https://chatbotmckinley.herokuapp.com/bot/schedule)
    `The schedule Message method gives user 2 functionalities`
    1) Schedule Message as a bot (Set is_user = False) : The message is scheduled using a date-time field which is converted into an epoch value at the backend
    2) Schedule Message as a user (Set is_user = True) : The message is scheduled using a date-time field which is converted into an epoch value at the backend
- [Join Conversation/Channel](https://chatbotmckinley.herokuapp.com/bot/coversation/)
    `The Join Conversation/Channel method allows the user to join a channel which they are not a part of using the conversation id`
- [List Conversation/Channel](https://chatbotmckinley.herokuapp.com/bot/coversation/list)
    `The List Conversation/Channel method allows the user to List all the channels in a workspace`
- [Slack Login](https://chatbotmckinley.herokuapp.com/slack/login)
    `Allows the user to login into their Slack account and recieve an access token in return`