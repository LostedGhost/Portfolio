# Generated by Django 5.0.6 on 2024-05-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rendu', '0008_counter_icone'),
    ]

    operations = [
        migrations.AddField(
            model_name='message_guess',
            name='lu',
            field=models.BooleanField(default=False),
        ),
    ]
