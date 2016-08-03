# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-03 07:59
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bodytext', models.TextField(verbose_name='Mensagem')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Postar em')),
                ('ip_address', models.GenericIPAddressField(default='0.0.0.0', verbose_name='Endereco IP')),
                ('user_name', models.CharField(default='anonymous', max_length=50, verbose_name='Nome de usuario')),
                ('user_email', models.EmailField(blank=True, max_length=254, verbose_name='E-mail do usuario')),
            ],
            options={
                'ordering': ['post_date'],
                'verbose_name': 'Comentario',
                'verbose_name_plural': 'Comentarios',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Titulo')),
                ('slug', models.SlugField(blank=True, null=True)),
                ('bodytext', models.TextField(verbose_name='Mensagem')),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Postar em')),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name='Modificado')),
                ('allow_comments', models.BooleanField(default=True, verbose_name='Permite comentarios')),
                ('comment_count', models.IntegerField(blank=True, default=0, verbose_name='Contagem de comentarios')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Imagem')),
                ('posted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Postado por')),
            ],
            options={
                'ordering': ['-post_date'],
                'verbose_name': 'post',
                'verbose_name_plural': 'posts',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post', verbose_name='Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
    ]
