from django.contrib import admin

from lionapp.models import *

admin.site.register(Post)
admin.site.register(Member)
admin.site.register(Comment)
admin.site.register(PostMember)
