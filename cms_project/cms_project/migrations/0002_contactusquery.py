# Generated by Django 2.2 on 2020-08-30 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUsQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=500)),
            ],
        ),
    ]
