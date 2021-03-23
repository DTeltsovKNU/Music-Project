from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

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

class SongsAdmin(ImportExportModelAdmin):
    inlines = [
        GenreInline,
        AlbumInline,
        CreatorInline,
    ]

class AlbumsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'release')

class ExportAdmin(ImportExportModelAdmin):
    pass



admin.site.register(Songsrelationships, ExportAdmin)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Creator, ExportAdmin)
admin.site.register(Albums, AlbumsAdmin)
admin.site.register(Users, ExportAdmin)
admin.site.register(Genre, ExportAdmin)

