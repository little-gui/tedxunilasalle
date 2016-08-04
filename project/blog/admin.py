from django.contrib import admin

from blog.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    fields = ('posted_by', 'post_date', 'title', 'subtitle', 'bodytext', 'image', 'allow_comments')
    list_display = ('title', 'subtitle', 'posted_by', 'comment_count', 'allow_comments')


class CommentAdmin(admin.ModelAdmin):
    fields = ('post', 'bodytext', 'user', 'user_name', 'user_email')
    list_display = ('post', 'bodytext', 'post_date', 'ip_address', 'user_name', 'user_email')


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
