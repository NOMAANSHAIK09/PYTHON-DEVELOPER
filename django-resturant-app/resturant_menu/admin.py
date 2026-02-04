from django.contrib import admin
from .models import item

class MenuitemAdmin(admin.ModelAdmin):
    list_display=("meal","status")
    list_filter=("status",)
    search_fields=("meal","description")


admin.site.register(item,MenuitemAdmin)
    
