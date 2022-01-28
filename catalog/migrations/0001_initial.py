# Generated by Django 4.0.1 on 2022-01-08 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите Имя', max_length=30, verbose_name='Имя')),
                ('last_name', models.CharField(help_text='Введите фамилию', max_length=30, verbose_name='Фамилия')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата Рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти', null=True, verbose_name='Дата смерти')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр книги')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=30, verbose_name='Язык книги')),
            ],
        ),
        migrations.CreateModel(
            name='MyModelName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field_name', models.CharField(help_text='Не более 20 символов', max_length=20)),
            ],
            options={
                'verbose_name': 'Название книги',
                'verbose_name_plural': 'Названия книг',
                'ordering': ['-my_field_name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('age', models.IntegerField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=50, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Введите ISBN книги', max_length=100, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора книги', to='catalog.Author', verbose_name='Aвтop книги')),
                ('genre', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre')),
                ('language', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language')),
            ],
        ),
    ]