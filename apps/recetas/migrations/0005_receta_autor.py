# Generated by Django 5.2.4 on 2025-07-29 12:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recetas', '0004_alter_comentario_options_alter_comentario_receta'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='receta',
            name='autor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='mis_recetas', to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
            preserve_default=False,
        ),
    ]
