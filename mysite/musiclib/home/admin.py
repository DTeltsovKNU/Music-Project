from django.contrib import admin
from .models import Songs, Songgeners, Creator, Creatorsongs, Songsrelationships, Albums, Albumsongs, Users, Usersongs, Genre

# Register your models here.

class SongsAdmin(admin.ModelAdmin):
    list_display = ('title', 'album', 'creator')

admin.site.register(Songsrelationships)
admin.site.register(Songs, SongsAdmin)
admin.site.register(Songgeners)
admin.site.register(Creator)
admin.site.register(Creatorsongs)
admin.site.register(Albums)
admin.site.register(Albumsongs)
admin.site.register(Users)
admin.site.register(Genre)
admin.site.register(Usersongs)

