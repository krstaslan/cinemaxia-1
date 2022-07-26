# Generated by Django 4.0.4 on 2022-07-21 09:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_movie_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rezervation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]