# Generated by Django 3.2.3 on 2021-08-13 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cis', '0003_auto_20210812_0917'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='case_inventory_found',
            field=models.CharField(default='Your Search is Found In Case Inventory Database', max_length=255),
        ),
    ]
