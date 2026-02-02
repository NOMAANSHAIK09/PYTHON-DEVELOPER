from django.contrib import admin
from .models import Form
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "occupation")
    list_filter = ("date", "occupation")
    
    readonly_fields = ("first_name", "last_name", "email", "date", "occupation")
admin.site.register(Form, FormAdmin)

# Register your models here.
