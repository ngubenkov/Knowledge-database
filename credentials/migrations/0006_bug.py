# Generated by Django 2.2.3 on 2019-07-18 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('credentials', '0005_auto_20190718_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('compnay', models.CharField(max_length=255)),
                ('user', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('version_of_module_software', models.CharField(blank=True, max_length=255, null=True)),
                ('solution_description', models.CharField(max_length=255)),
                ('solved', models.BooleanField(max_length=255)),
                ('who_is_solving_it', models.CharField(blank=True, max_length=255, null=True)),
                ('release_on_beta', models.BooleanField(max_length=255)),
                ('release_on_official', models.BooleanField(max_length=255)),
                ('database_version', models.CharField(max_length=255)),
                ('software_version', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('date_entered', models.DateField(max_length=255)),
                ('date_solved', models.DateField(max_length=255)),
            ],
            options={
                'ordering': ('solved', 'date_entered'),
            },
        ),
    ]
