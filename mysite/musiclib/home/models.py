from django.db import models

class Albumsongs(models.Model):
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    albumid = models.IntegerField(db_column='AlbumId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlbumSongs'


class Albums(models.Model):
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    amount_of_songs = models.IntegerField(db_column='Amount_of_songs', blank=True, null=True)  # Field name made lowercase.
    release = models.DateField(db_column='Release', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Albums'


class Creator(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Creator'


class Creatorsongs(models.Model):
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='CreatorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreatorSongs'


class Genre(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genre'


class Songgeners(models.Model):
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, db_column='GenreId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongGeners'


class Songs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50)  # Field name made lowercase.
    release = models.DateField(db_column='Release', blank=True, null=True)  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    cover = models.TextField(db_column='Cover')  # Field name made lowercase.
    creator = models.CharField(db_column='Creator', max_length=50, blank=True, null=True)  # Field name made lowercase.
    album = models.CharField(db_column='Album', max_length=50, blank=True, null=True)  # Field name made lowercase.
    genre = models.CharField(db_column='Genre', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.title
            
    
    class Meta:
        verbose_name='Песни'
        managed = False
        db_table = 'Songs'
        


class Songsrelationships(models.Model):
    song1 = models.IntegerField(db_column='Song1')  # Field name made lowercase.
    song2 = models.ForeignKey(Songs, models.DO_NOTHING, db_column='Song2')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SongsRelationships'


class Usersongs(models.Model):
    songid = models.ForeignKey(Songs, models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserSongs'


class Users(models.Model):
    name = models.CharField(db_column='Name', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Users'
