# Generated by Django 2.2.10 on 2020-05-10 23:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0003_auto_20200510_1957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estado',
            name='sigla',
            field=models.CharField(max_length=2),
        ),
    ]