from django.db import models
from django.db.models import CharField
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text=" Введите жанр книги", verbose_name="Жанр книги")

    def __str__(self):
        return self.name

class Language(models.Model):
    name = models.CharField(max_length=200, help_text=" Введите язык книги", verbose_name="Язык книги")

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(help_text="Введите дату рождения", verbose_name="Дата рождения", null=True, blank=True)
    date_of_death = models.DateField(help_text="Введите дату смерти", verbose_name="Дата смерти", null=True, blank=True)

    def __str__(self):
        return self.last_name

class Book(models.Model):
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, help_text="Выберите жанр для книги", verbose_name="Жанр книги", null=True)
    language = models.ForeignKey('Language', on_delete=models.CASCADE, help_text="Выберите язык для книги", verbose_name="Язык книги", null=True)
    author = models.ManyToManyField('Author', help_text="Выберите автора книги", verbose_name="Автор книги")
    summary = models.TextField(max_length=1000, help_text="Введите краткое описание книги", verbose_name="Аннотация книги")
    isbn = models.CharField(max_length=13, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])

    def display_author(self):
        return ', '.join([author.last_name for author in
                          self.author.all()])
    display_author.short_description = 'Авторы'


class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги", verbose_name="Статус экземпляра книги")

    def __str__(self):
        return self.name

class BookInstance(models.Model):
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите инвентарный номер книги", verbose_name="Инвентарный номер книги")
    imprint = models.CharField(max_length=200, help_text="Введите издательство и год выпуска", verbose_name="Издательство")
    status = models.ForeignKey('Status', on_delete=models.CASCADE, null=True, help_text='Изменить состояние экземпляра', verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True, blank=True, help_text="Введите конец срока статуса", verbose_name="Дата окончания статуса")

    def __str__(self):
        return '%s %s %s' %(self.inv_nom, self.book, self.status)

class Lecturer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    lecturer = models.ForeignKey('Lecturer', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Group(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    students = models.ManyToManyField('Student')

    def __str__(self):
        return self.name

class Task(models.Model):
    task = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    date = models.DateField()