# Generated by Django 2.2.3 on 2019-07-18 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0002_auto_20190718_0848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='activate_day',
            field=models.DateField(max_length=255),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='expire_day',
            field=models.DateField(max_length=255),
        ),
    ]
