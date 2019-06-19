# Generated by Django 2.2 on 2019-06-18 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('code', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='CustBranch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('contact', models.CharField(max_length=200)),
                ('billing_street', models.CharField(max_length=200)),
                ('billing_city', models.CharField(max_length=200)),
                ('billing_state', models.CharField(max_length=200)),
                ('billing_zip_code', models.CharField(max_length=200)),
                ('billing_country', models.CharField(max_length=200)),
                ('shipping_street', models.CharField(max_length=200)),
                ('shipping_city', models.CharField(max_length=200)),
                ('shipping_zip_code', models.CharField(max_length=200)),
                ('shipping_country', models.CharField(max_length=200)),
                ('debtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.Debtor')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]