from django.contrib import admin
from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'quantity', 'category')
    list_display_links = ('id', 'title')
    list_filter = ('category',)
    list_editable = ('is_published',)
    search_fields = ('title',)
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)
