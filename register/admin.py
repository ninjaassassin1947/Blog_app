from django.contrib import admin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # Define which fields to display in the list view
    list_display = ('username', 'email', 'created_at', 'is_staff', 'is_superuser')

    # Define which fields to include in the detail view (form view)
    fields = ('username', 'email','password', 'bio', 'created_at','profile_image')

    # Optional: Define which fields are editable in the admin panel
    readonly_fields = ('created_at',)  # Make `created_at` read-only

    # Optional: Define search fields
    search_fields = ('username', 'email')

    # Optional: Define filter options
    list_filter = ('created_at',)
