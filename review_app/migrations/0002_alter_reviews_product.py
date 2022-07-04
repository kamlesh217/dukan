# Generated by Django 4.0 on 2022-07-04 12:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0005_delete_reviews'),
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product_app.product_table'),
        ),
    ]
