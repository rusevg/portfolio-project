# Generated by Django 4.0.5 on 2022-07-09 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('our_portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description',
            field=models.CharField(default=123, max_length=250),
            preserve_default=False,
        ),
    ]
