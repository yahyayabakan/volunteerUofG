# Generated by Django 4.0.6 on 2022-07-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteerUofG', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
