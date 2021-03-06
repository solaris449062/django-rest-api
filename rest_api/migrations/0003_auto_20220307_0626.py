# Generated by Django 2.2 on 2022-03-07 06:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0002_profilefeeditem'),
    ]

    operations = [
        migrations.AddField(
            model_name='profilefeeditem',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profilefeeditem',
            name='status_text',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
