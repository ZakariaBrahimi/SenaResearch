# Generated by Django 4.1.7 on 2023-06-16 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sena_research', '0003_alter_order_promoter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='promoter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='sena_research.service'),
        ),
    ]
