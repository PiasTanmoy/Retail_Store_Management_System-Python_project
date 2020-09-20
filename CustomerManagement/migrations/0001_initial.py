# Generated by Django 3.1.1 on 2020-09-20 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_name', models.CharField(max_length=100)),
                ('Last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200, unique=True)),
                ('phn_no', models.IntegerField(blank=True, null=True)),
                ('Street', models.CharField(max_length=200)),
                ('City', models.CharField(max_length=100)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Products_points', models.IntegerField(blank=True)),
                ('customers', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CustomerManagement.customer')),
            ],
        ),
    ]
