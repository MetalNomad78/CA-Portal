# Generated by Django 3.2.9 on 2022-08-12 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0006_auto_20220812_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='question',
            field=models.TextField(blank=True),
        ),
    ]
