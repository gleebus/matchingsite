# Generated by Django 2.1.3 on 2018-11-25 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matchingapp', '0009_conversation_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='contents',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
