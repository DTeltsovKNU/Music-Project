from django.db import models



class Albums(models.Model):
    title = models.CharField(db_column='Title', max_length=50, verbose_name='Название')  # Field name made lowercase.
    amount_of_songs = models.IntegerField(db_column='Amount_of_songs', blank=True, null=True,verbose_name='Количество песен')  # Field name made lowercase.
    release = models.DateField(db_column='Release', blank=True, null=True, verbose_name='Дата релиза')  # Field name made lowercase.

    def __str__(self):
        return self.title
            
    
    class Meta:
        verbose_name='Альбом'
        verbose_name_plural = 'Альбомы' 
        managed = False
        db_table = 'Albums'

class Albumsongs(models.Model):
    albumid = models.ForeignKey(Albums, models.DO_NOTHING, db_column='albumid', blank=True, null=True)
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='songid', blank=True, null=True)

    class Meta:
        verbose_name='Альбом'
        verbose_name_plural = 'Альбом' 
        managed = False
        db_table = 'Albumsongs'

class Creator(models.Model):
    name = models.CharField(db_column='Name', max_length=50, verbose_name='Название')  # Field name made lowercase. # Field name made lowercase.

    def __str__(self):
        return self.name
            
    class Meta:
        verbose_name='Автор'
        verbose_name_plural = 'Авторы' 
        managed = False
        db_table = 'Creator'


class Creatorsongs(models.Model):
    creatorid = models.ForeignKey(Creator, models.DO_NOTHING, db_column='creatorid', blank=True, null=True)
    songid = models.ForeignKey('Songs', models.DO_NOTHING, db_column='songid', blank=True, null=True)

    class Meta:
        verbose_name='Автор'
        verbose_name_plural = 'Автор' 
        managed = False
        db_table = 'Creatorsongs'


class Genre(models.Model):
    name = models.CharField(db_column='Name', max_length=50, verbose_name='Название')  # Field name made lowercase.

    def __str__(self):
        return self.name
            
    
    class Meta:
        verbose_name='Жанр'
        verbose_name_plural = 'Жанры' 
        managed = False
        db_table = 'Genre'


class Songs(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=50, verbose_name='Название')  # Field name made lowercase.
    release = models.DateField(db_column='Release', blank=True, null=True, verbose_name='Дата релиза')  # Field name made lowercase.
    text = models.TextField(db_column='Text', blank=True, null=True, verbose_name='Текст')  # Field name made lowercase. This field type is a guess.
    cover = models.TextField(db_column='Cover', blank=True, null=True, verbose_name='Обложка')  # Field name made lowercase.

    def __str__(self):
        return self.title

    
    class Meta:
        verbose_name='Песня'
        verbose_name_plural = 'Песни' 
        managed = False
        db_table = 'Songs'
        ordering = ('-title',)

        
class Songsgenre(models.Model):
    songid = models.ForeignKey(Songs, models.DO_NOTHING, db_column='songid')
    genreid = models.ForeignKey(Genre, models.DO_NOTHING, db_column='genreid')

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural = 'Жанр' 
        managed = False
        db_table = 'SongsGenre'


class Songsrelationships(models.Model):
    song1 = models.IntegerField(db_column='Song1')  # Field name made lowercase.
    song2 = models.ForeignKey(Songs, models.DO_NOTHING, db_column='Song2')  # Field name made lowercase.
    status = models.TextField(db_column='Status')  # Field name made lowercase. This field type is a guess.

    
    class Meta:
        verbose_name='Схожая песня'
        verbose_name_plural = 'Схожие песни' 
        managed = False
        db_table = 'SongsRelationships'



class Users(models.Model):
    name = models.CharField(db_column='Name', max_length=50, verbose_name='Логин')  # Field name made lowercase. # Field name made lowercase.  # Field name made lowercase.

    def __str__(self):
        return self.name
            
    
    class Meta:
        verbose_name='Пользователь'
        verbose_name_plural = 'Пользователи' 
        managed = False
        db_table = 'Users'


class Usersongs(models.Model):
    userid = models.ForeignKey(Users, models.DO_NOTHING, db_column='userid', blank=True, null=True)
    songid = models.ForeignKey(Songs, models.DO_NOTHING, db_column='songid', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usersongs'
