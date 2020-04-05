# Generated by Django 3.0.3 on 2020-03-11 03:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aluno', '0006_aluno_plano'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='acesso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='aluno',
            name='endereco',
            field=models.CharField(max_length=70),
        ),
    ]