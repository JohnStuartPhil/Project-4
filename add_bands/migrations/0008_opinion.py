# Generated by Django 4.2.19 on 2025-03-23 21:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('add_bands', '0007_alter_post_genre_alter_post_number_of_members'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks_out_of_five', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('your_thoughts', models.TextField(unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('approved', models.BooleanField(default=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinionator', to=settings.AUTH_USER_MODEL)),
                ('band', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='add_bands.post')),
            ],
        ),
    ]
