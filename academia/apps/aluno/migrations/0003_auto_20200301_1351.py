# Generated by Django 3.0.3 on 2020-03-01 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aluno', '0002_auto_20200301_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='plano',
            field=models.CharField(help_text='1-Mensal ou 2-Anual', max_length=1),
        ),
    ]