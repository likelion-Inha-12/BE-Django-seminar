from typing import Any
from django.db import models

class Member(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(unique = True)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length = 50)
    member_id = models.ForeignKey(Member, verbose_name="글 작성자", on_delete=models.DO_NOTHING)
    content = models.TextField(null = True, blank = True)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.CharField(max_length = 200, null = True, blank = True)
    member_id = models.ForeignKey(Member, verbose_name="댓글 작성자", on_delete=models.CASCADE, related_name="comments")
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return self.content

class PostMember(models.Model):
    post_id = models.ForeignKey(Post, verbose_name="Post", on_delete=models.CASCADE)
    member_id = models.ForeignKey(Member, verbose_name="글 작성자", on_delete=models.DO_NOTHING)

