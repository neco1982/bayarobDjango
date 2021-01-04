from django.contrib import admin
from .models import Author, Category, Project, Comment
from embed_video.admin import AdminVideoMixin

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Project, MyModelAdmin)
admin.site.register(Comment)

