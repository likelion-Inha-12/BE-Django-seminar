from django.contrib import admin

from lionapp.models import Post
from users.models import User

admin.site.register(Post)
admin.site.register(User)