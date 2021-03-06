# Generated by Django 2.2.3 on 2019-07-18 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0003_auto_20190718_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='activate_day',
            field=models.DateField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='allowed_users',
            field=models.IntegerField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='company_phone',
            field=models.IntegerField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='expire_day',
            field=models.DateField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='installed_users',
            field=models.IntegerField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='licence_key',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='windows_password',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='credentials',
            name='windows_username',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
