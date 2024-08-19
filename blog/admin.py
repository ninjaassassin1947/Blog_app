from django.contrib import admin
from .models import Post, Comment ,Category

# BLOG POST ADMIN


class CustomPostAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('title',  'id','published' )

    # Define which fields to include in the detail view (form view)
    fields = ('title', 'cover_image','content', 'slug', 'published', 'updated_at','author','category')

    # Optional: Define which fields are editable in the admin panel
    readonly_fields = ('published','updated_at')  # Make `created_at` read-only

    # Optional: Define search fields
    search_fields = ('title', )

    # Optional: Define filter options
    list_filter = ('published',)

admin.site.register(Post, CustomPostAdmin)


# COMMENT ADMIN


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created_on')
    list_filter = ('created_on',)  # Added a comma to make it a tuple
    search_fields = ('user__username', 'body')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    prepopulated_fields = {'slug': ('name',)}



