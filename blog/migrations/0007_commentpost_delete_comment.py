# Generated by Django 4.0.5 on 2022-07-18 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField(verbose_name='Text of comment')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('moderation', models.BooleanField(default=False)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.blog')),
            ],
            options={
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
                'db_table': 'comments',
            },
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
