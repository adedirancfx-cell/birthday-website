from django.contrib import admin
from .models import Photo, LoveMessage, BirthdayWish, PickupLine

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_favorite']
    list_editable = ['order', 'is_favorite']
    list_filter = ['is_favorite']
    search_fields = ['title', 'caption']

@admin.register(LoveMessage)
class LoveMessageAdmin(admin.ModelAdmin):
    list_display = ['created_at', 'message_preview']
    
    def message_preview(self, obj):
        return obj.message[:50] + "..." if len(obj.message) > 50 else obj.message

@admin.register(BirthdayWish)
class BirthdayWishAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name', 'message']

# FIXED ADMIN FOR PICKUP LINES
@admin.register(PickupLine)
class PickupLineAdmin(admin.ModelAdmin):
    list_display = ['order', 'question', 'is_active', 'id']
    list_display_links = ['question']  # This fixes the error - makes 'question' clickable
    list_editable = ['order', 'is_active']  # Now these can be edited inline
    list_filter = ['is_active']
    search_fields = ['question', 'sweet_response']
    fieldsets = (
        ('Question Settings', {
            'fields': ('order', 'question', 'is_active')
        }),
        ('Answer Settings', {
            'fields': ('expected_keywords', 'sweet_response', 'hint'),
            'description': 'Enter keywords that will trigger the sweet response (comma-separated)'
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.hint:
            obj.hint = f"Try typing something like: {obj.expected_keywords.split(',')[0]}"
        super().save_model(request, obj, form, change)