# Generated by Django 3.0.6 on 2020-12-18 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_help'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
