# Generated by Django 3.1.12 on 2021-06-21 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_embedding'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
    ]
