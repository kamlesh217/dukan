# Generated by Django 4.0.5 on 2022-07-06 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0006_alter_category_group_category_group_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_table',
            name='brand',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='product_table',
            name='tags',
            field=models.TextField(default='', null=True),
        ),
    ]