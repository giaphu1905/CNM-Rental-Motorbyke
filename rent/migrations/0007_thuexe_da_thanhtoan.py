# Generated by Django 5.0.4 on 2024-05-04 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0006_phukien'),
    ]

    operations = [
        migrations.AddField(
            model_name='thuexe',
            name='da_thanhtoan',
            field=models.BooleanField(default=False),
        ),
    ]
