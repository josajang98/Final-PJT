from django.contrib import admin
from .models import WishList
# Register your models here.

class WishListAdmin(admin.ModelAdmin):
    list_display = ('user','movie_id')


admin.site.register(WishList,WishListAdmin)