# Generated by Django 4.0.5 on 2022-07-22 08:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_commentpost_delete_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='commentpost',
            old_name='blog',
            new_name='blog_c',
        ),
    ]