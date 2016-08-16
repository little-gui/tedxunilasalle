from django.db.models.signals import post_save
from django.utils.text import slugify

from .models import Post, Comment


def save_comment(sender, instance, created, **kwargs):
    if created:
        comment = instance
        post = comment.post
        post.comment_count = post.comments.count()
        post.save(force_update=True)


def save_slug(sender, instance, **kwargs):
	instance.slug = slugify(instance.title)
	
