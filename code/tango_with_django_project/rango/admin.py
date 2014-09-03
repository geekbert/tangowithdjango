from django.contrib import admin

# Register your models here.

from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)

# To customise the admin interface, you will need to edit rango/admin.py and create a PageAdmin class that inherits from admin.ModelAdmin

#class PageAdmin(admin.ModelAdmin):    
#    list_display = ('title', 'category')

#admin.site.register(PageAdmin)
