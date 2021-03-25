from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.utils.safestring import mark_safe

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


@admin.register(Songs)
class SongsAdmin(ImportExportModelAdmin):
    inlines = [
        GenreInline,
        AlbumInline,
        CreatorInline,
    ]
    search_fields = ['title']
    list_display = ('title', 'get_img')

    def get_img(self, obj):
        return mark_safe(f'<img src = {obj.cover} width = "50" height = "50"')

    get_img.short_description = 'Обложка'

@admin.register(Albums)
class AlbumsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'release')
    list_filter = ['amount_of_songs']
    search_fields = ['title']

    change_list_template = 'admin\home\Albums\change_list.html'

    def changelist_view(self, request, extra_context=None):
        # Aggregate new subscribers per day
        data = Albums.objects.all()
        context = {
            'data':data
        }

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=context)


class ExportAdmin(ImportExportModelAdmin):
    pass



admin.site.register(Songsrelationships, ExportAdmin)
admin.site.register(Creator, ExportAdmin)
admin.site.register(Users, ExportAdmin)
admin.site.register(Genre, ExportAdmin)

