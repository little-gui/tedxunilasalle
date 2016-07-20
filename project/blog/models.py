# -*- coding: utf-8 -*-
from django.db import models
from django.db.models.signals import post_save
from django.core.urlresolvers import reverse
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name=_("Titulo"))
    slug = models.SlugField()
    bodytext = models.TextField(verbose_name=_("Mensagem"))

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Postar em"))
    modified = models.DateTimeField(null=True, verbose_name=_("Modificado"))
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Postado por"))

    allow_comments = models.BooleanField(
        default=True, verbose_name=_("Permite comentários"))
    comment_count = models.IntegerField(
        blank=True, default=0, verbose_name=_('Contagem de comentários'))

    class Meta:
        verbose_name = _('post')
        verbose_name_plural = _('posts')
        ordering = ['-post_date']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        kwargs = {
            'slug': self.slug,
            'year': '%04d' % self.post_date.year,
            'month': '%02d' % self.post_date.month,
            'day': '%02d' % self.post_date.day,
        }

        return reverse('blog_detail', kwargs=kwargs)


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='comments', verbose_name=_("Post"))
    bodytext = models.TextField(verbose_name=_("Mensagem"))

    post_date = models.DateTimeField(
        auto_now_add=True, verbose_name=_("Postar em"))
    ip_address = models.GenericIPAddressField(
        default='0.0.0.0', verbose_name=_("Endereço IP"))

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True, verbose_name=_("Usuário"), related_name='comment_user')
    user_name = models.CharField(
        max_length=50, default='anonymous', verbose_name=_("Nome de usuário"))
    user_email = models.EmailField(blank=True, verbose_name=_("E-mail do usuário"))

    class Meta:
        verbose_name = _('Comentário')
        verbose_name_plural = _('Comentários')
        ordering = ['post_date']

from blog.signals import save_comment

post_save.connect(save_comment, sender=Comment)