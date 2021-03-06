# Generated by Django 3.1.7 on 2021-02-25 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('amount_of_songs', models.IntegerField(db_column='Amount_of_songs')),
                ('release', models.DateField(db_column='Release')),
            ],
            options={
                'db_table': 'Albums',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Albumsongs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('albumid', models.IntegerField(db_column='AlbumId')),
            ],
            options={
                'db_table': 'AlbumSongs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
            ],
            options={
                'db_table': 'Creator',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Creatorsongs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'CreatorSongs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('songid', models.IntegerField(db_column='SongId')),
            ],
            options={
                'db_table': 'Genre',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songgeners',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'SongGeners',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.TextField(db_column='Name')),
                ('release', models.DateField(db_column='Release')),
                ('text', models.TextField(db_column='Text')),
            ],
            options={
                'db_table': 'Songs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Songsrelationships',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('song1', models.IntegerField(db_column='Song1')),
                ('status', models.TextField(db_column='Status')),
            ],
            options={
                'db_table': 'SongsRelationships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'Users',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Usersongs',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'UserSongs',
                'managed': False,
            },
        ),
    ]
