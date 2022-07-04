# Generated by Django 4.0 on 2022-07-04 09:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product_app', '0002_remove_location_table_location_holder'),
        ('user_app', '0002_custom_user_id_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='custom_user',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product_app.location_table'),
        ),
    ]