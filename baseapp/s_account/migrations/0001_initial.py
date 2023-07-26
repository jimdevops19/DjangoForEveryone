# Generated by Django 4.2.2 on 2023-07-18 05:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('region_name', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('zone_name', models.CharField(default='', max_length=50)),
                ('region_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.region')),
            ],
        ),
        migrations.CreateModel(
            name='Wereda',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Wereda_name', models.CharField(default='', max_length=50)),
                ('region_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.region')),
                ('zone_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.zone')),
            ],
        ),
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_name', models.CharField(default='', max_length=50)),
                ('Wereda_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.wereda')),
                ('region_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.region')),
                ('zone_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='s_account.zone')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateTimeField()),
                ('gender', models.CharField(choices=[('malle', 'M'), ('FEMALE', 'F')], max_length=6)),
                ('user_type', models.CharField(choices=[('federal_admin', 'Federal Admin'), ('regional_admin', 'regional admin'), ('zone_admin', 'zone admin'), ('wereda_admin', 'wereda admin'), ('building_admin', 'building admin'), ('stock_admin', 'stock admin'), ('stock_personnel', 'stock personnel')], max_length=50)),
                ('Wereda_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='s_account.wereda')),
                ('Zone_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='s_account.zone')),
                ('region_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='s_account.region')),
                ('stock_name', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='s_account.stock')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
