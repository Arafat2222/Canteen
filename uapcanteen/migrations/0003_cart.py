# Generated by Django 5.0.4 on 2024-04-23 08:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uapcanteen', '0002_breakfast_dinner_lunch'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('total_price', models.IntegerField()),
                ('discount', models.IntegerField()),
                ('breakfast', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uapcanteen.breakfast')),
                ('dinner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uapcanteen.dinner')),
                ('lunch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='uapcanteen.lunch')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
