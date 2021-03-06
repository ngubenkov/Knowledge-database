# Generated by Django 2.2.3 on 2019-07-18 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0004_auto_20190718_0943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='activate_day',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='allowed_users',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='company_phone',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='expire_day',
            field=models.DateField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='installed_users',
            field=models.IntegerField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='licence_key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='windows_password',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='windows_username',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
