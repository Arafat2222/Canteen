# Generated by Django 5.0.4 on 2024-05-13 16:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapcanteen', '0007_remove_cart_lunch_remove_order_breakfast_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='lunch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uapcanteen.lunch'),
        ),
    ]