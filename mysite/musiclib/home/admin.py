from django.contrib import admin
from .models import *

# Register your models here.


class GenreInline(admin.TabularInline):
    model = Songsgenre
    extra = 1   

class CreatorInline(admin.TabularInline):
    model = Creatorsongs
    extra = 1  

class AlbumInline(admin.TabularInline):
    model = Albumsongs
    extra = 1  

class SongsAdmin(admin.ModelAdmin):
    inlines = [
        GenreInline,
        AlbumInline,
        CreatorInline,
    ]

class AlbumsAdmin(admin.ModelAdmin):
    list_display = ('title', 'release')


admin.site.register(Songsrelationships)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Creator)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Users)
admin.site.register(Genre)

