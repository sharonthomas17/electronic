# Generated by Django 3.2 on 2022-08-16 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='elect_shop',
            name='sh_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.shop'),
        ),
    ]