from django.contrib import admin

# Register your models here.
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'audience', 'release_date', 'genre', 'score', 'poster_url', 'description',)

admin.site.register(Movie, MovieAdmin)