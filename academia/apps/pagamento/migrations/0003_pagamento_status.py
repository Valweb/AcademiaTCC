# Generated by Django 3.0.3 on 2020-03-14 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagamento', '0002_auto_20200301_1353'),
    ]

    operations = [
        migrations.AddField(
            model_name='pagamento',
            name='status',
            field=models.CharField(choices=[('1', 'Pago'), ('2', 'Aberto')], default=1, max_length=1),
            preserve_default=False,
        ),
    ]