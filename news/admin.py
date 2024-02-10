from django.contrib import admin
from .models import *


# Register your models here.

# for configuration of Category admin
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('image_tag', 'title', 'description', 'add_date')
#     search_fields = ('title',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50
# E:\myprojects\holoproject\news\static\assets\js
    class Media:
        js = ('assets/js/script.js',)

# 'https://cdn.tiny.cloud/1/no-api-key/tinymce/5/tinymce.min.js',
admin.site.register(Category,)  # CategoryAdmin
admin.site.register(Dailynews, PostAdmin),
admin.site.register(Weeklynews),
admin.site.register(vedio),
admin.site.register(sidecontent),
admin.site.register(politics),
admin.site.register(newnewsforegin),
