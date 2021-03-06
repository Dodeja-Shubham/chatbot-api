# Generated by Django 3.1.1 on 2020-09-25 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('botuser', '0003_schedule_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conversation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conversation_id', models.CharField(max_length=100)),
                ('conversation_name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
