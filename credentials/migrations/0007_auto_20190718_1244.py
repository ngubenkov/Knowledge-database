# Generated by Django 2.2.3 on 2019-07-18 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0006_bug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
