# Generated by Django 4.2.2 on 2023-07-24 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_department_sectors_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('malle', 'Male'), ('FEMALE', 'Female')], max_length=6),
        ),
    ]
