# Generated by Django 2.0.7 on 2019-07-02 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_auto_20190702_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manhattan',
            name='SALE_DATE',
            field=models.DateField(),
        ),
    ]
