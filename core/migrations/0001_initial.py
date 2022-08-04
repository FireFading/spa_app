# Generated by Django 4.1 on 2022-08-04 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("h1", models.CharField(max_length=200)),
                ("title", models.CharField(max_length=200)),
                ("url", models.SlugField()),
                ("description", models.TextField()),
                ("content", models.TextField()),
                ("image", models.ImageField(upload_to="")),
                ("created_at", models.DateField(default=django.utils.timezone.now)),
                ("tag", models.CharField(max_length=200)),
                (
                    "author",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
