# Generated by Django 5.0.4 on 2024-05-02 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0003_alter_xemay_ten'),
    ]

    operations = [
        migrations.AddField(
            model_name='xemay',
            name='loai_xe',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
