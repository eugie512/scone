from listings.models import Listing
from django.contrib import admin

class ListingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['title','city','price']}),
        (None,               {'fields': ['description']}),
        ('Date information', {'fields': ['list_date']}),
    ]
    list_display = ('title', 'price', 'list_date')
    list_filter = ['list_date']
    search_fields = ['title','price']

admin.site.register(Listing, ListingAdmin)