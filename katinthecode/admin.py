from django.contrib import admin
from .models import Post, Post_Tag, Post_Image

# admin.site.register(Post)
# admin.site.register(Post_Tag)
# admin.site.register(Post_Image)

class PostTagInline(admin.TabularInline):
    model = Post_Tag
    extra = 1
    
class PostImageInline(admin.TabularInline):
    model = Post_Image
    extra = 1

class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'description', 'post_text']
    list_display = ('title', 'description', 'insert_date', 'update_date')
    list_filter = ['update_date']
    search_fields = ['title', 'description']
    inlines = [PostTagInline, PostImageInline]
    
admin.site.register(Post, PostAdmin)