# Generated by Django 4.2 on 2024-03-09 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_moto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('milage', models.PositiveIntegerField(verbose_name='пробег')),
                ('year', models.PositiveSmallIntegerField(verbose_name='год регистрации')),
                ('car', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.car')),
                ('moto', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.moto')),
            ],
            options={
                'verbose_name': 'пробег',
                'verbose_name_plural': 'пробег',
                'ordering': ('-year',),
            },
        ),
    ]
