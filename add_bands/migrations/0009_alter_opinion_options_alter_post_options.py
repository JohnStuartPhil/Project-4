# Generated by Django 4.2.19 on 2025-03-25 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('add_bands', '0008_opinion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='opinion',
            options={'ordering': ['created_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_on']},
        ),
    ]
