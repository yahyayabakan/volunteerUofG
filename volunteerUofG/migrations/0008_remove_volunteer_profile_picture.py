# Generated by Django 4.0.6 on 2022-08-02 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerUofG', '0007_alter_charity_image_alter_opportunity_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteer',
            name='profile_picture',
        ),
    ]