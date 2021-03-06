# Generated by Django 3.1.1 on 2020-09-20 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_status', models.CharField(default='Order Status', max_length=200)),
                ('Order_date', models.DateField(blank=True)),
                ('Require_date', models.DateField(blank=True)),
                ('Shipped_date', models.DateField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True)),
                ('price_each', models.IntegerField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Invoice_num', models.IntegerField(blank=True)),
                ('payment_date', models.DateField(blank=True)),
                ('Amount', models.IntegerField(blank=True)),
            ],
        ),
    ]
