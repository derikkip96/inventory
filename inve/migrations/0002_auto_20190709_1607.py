# Generated by Django 2.2 on 2019-07-09 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemunit',
            name='inactive',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='tax',
            name='defaults',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
        migrations.AlterField(
            model_name='tax',
            name='excempt',
            field=models.BooleanField(choices=[(False, 'No'), (True, 'Yes')], default=False),
        ),
    ]
