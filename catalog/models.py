from django.db import models
from django.shortcuts import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Введите жанр книги', verbose_name='Жанр книги')


    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'
        ordering = ['-name']

    # def get_absolute_url(self):
    #     return reverse('detail-genre', args=[str(self.id)])

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=30, help_text='Введите язык книги', verbose_name='Язык книги')

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя',
                                  help_text='Введите Имя')

    last_name = models.CharField(max_length=30, verbose_name='Фамилия',
                                 help_text='Введите фамилию')

    date_of_birth = models.DateField(verbose_name='Дата Рождения', help_text="Введите дату рождения",
                                     null=True, blank=True)

    date_of_death = models.DateField(verbose_name='Дата смерти', help_text='Введите дату смерти',
                                     null=True, blank=True)
    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'
    def __str__(self):
        return self.last_name


class Books(models.Model):
    title = models.CharField(max_length=50, help_text='Введите название книги', verbose_name='Название книги')
    author = models.ManyToManyField('Author',
                                    help_text="Выберите автора книги",
                                    verbose_name="Aвтop книги")

    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    summary = models.TextField(max_length=1000, verbose_name='Аннотация книги', help_text='Введите краткое описание книги')
    isbn = models.CharField(max_length=100, help_text='Введите ISBN книги', verbose_name='ISBN книги')
    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'


    def display_authors(self):
        return ', '.join([i.last_name for i in self.author.all()])

    def something(self):
        return 'something str'

    something.short_description = 'Hello, this title new row'
    display_authors.short_description = 'Авторы'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])




class MyModelName(models.Model):
    my_field_name = models.CharField(max_length=20, help_text='Не более 20 символов')

    class Meta:
        ordering = ["-my_field_name"]
        verbose_name = 'Название книги'
        verbose_name_plural = 'Названия книг'

    def get_absolute_url(self):
        # Возвращает url-aдpec для доступа к экземпляру MyModelName
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.my_field_name

class Person(models.Model):
    choice = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    name = models.CharField(max_length=140)
    age = models.IntegerField()
    sex = models.CharField(max_length=1, choices=choice)

    def get_absolute_url(self):
        return reverse('myurl', kwargs={'id': self.id, 'name': self.name})


    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=30, help_text='Введите статус экземпляра книги',
                            verbose_name='Статус экземпляра книги')

    class Meta:
        verbose_name = 'Статус книги'
        verbose_name_plural = 'Статус книг'

    def __str__(self):
        return self.name


class BookInstance(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    inv_nom = models.CharField(max_length=30, help_text='Введите инвентарный номер книги',
                               verbose_name='Инвентарный номер')
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    imprint = models.CharField(max_length=200, help_text='Введите издательство и год выпуска',
                               verbose_name='Издательство')
    due_back = models.DateField(verbose_name='Дата окончания статуса',
                                help_text='Введите дату окончания статуса')

    def __str__(self):
        return f'N {self.inv_nom} book: {self.book} статус: {self.status}'
