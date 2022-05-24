from django.contrib import admin
from .models import Review

# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user','movie_id','title','content','rate')

admin.site.register(Review,ReviewAdmin)