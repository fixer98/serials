from django.contrib import admin
from ser.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('name_ru', 'seasons')

admin.site.register(Post, PostAdmin)