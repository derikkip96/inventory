# Generated by Django 2.2 on 2019-07-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salestype',
            name='default',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')]),
        ),
    ]