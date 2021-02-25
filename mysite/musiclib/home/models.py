from django.db import models

class Albumsongs(models.Model):
    id = models.IntegerField(primary_key=True)
    songid = models.ForeignKey('Albums', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    albumid = models.IntegerField(db_column='AlbumId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AlbumSongs'


class Albums(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    amount_of_songs = models.IntegerField(db_column='Amount_of_songs')  # Field name made lowercase.
    release = models.DateField(db_column='Release')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Albums'


class Creator(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Creator'


class Creatorsongs(models.Model):
    id = models.IntegerField(primary_key=True)
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='CreatorId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CreatorSongs'


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    songid = models.IntegerField(db_column='SongId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Genre'


class Songgeners(models.Model):
    id = models.IntegerField(primary_key=True)
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, db_column='GenreId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SongGeners'


class Songs(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(db_column='Name')  # Field name made lowercase. This field type is a guess.
    release = models.DateField(db_column='Release')  # Field name made lowercase.
    text = models.TextField(db_column='Text')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'Songs'


class Songsrelationships(models.Model):
    id = models.IntegerField(primary_key=True)
    song1 = models.IntegerField(db_column='Song1')  # Field name made lowercase.
    song2 = models.ForeignKey(Songs, models.DO_NOTHING, db_column='Song2')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'SongsRelationships'



class Usersongs(models.Model):
    id = models.IntegerField(primary_key=True)
    songid = models.ForeignKey(Songs, models.DO_NOTHING, db_column='SongId')  # Field name made lowercase.
    userid = models.ForeignKey('Users', models.DO_NOTHING, db_column='UserId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'UserSongs'


class Users(models.Model):
    id = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'Users'

