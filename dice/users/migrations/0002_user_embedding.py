# Generated by Django 3.1.12 on 2021-06-22 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='embedding',
            field=models.JSONField(blank=True, null=True, verbose_name='User Embedding'),
        ),
    ]
