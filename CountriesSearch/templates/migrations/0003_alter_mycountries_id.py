# Generated by Django 5.0.3 on 2024-10-05 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0002_alter_mycountries_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mycountries',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
