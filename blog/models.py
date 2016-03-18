from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[self.post_id])





