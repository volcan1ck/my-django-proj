from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import FormTask
from .models import Lecturer, Book, BookInstance, Author, Group, Student, Task
from django.views import generic


def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact=2).count()
    num_authors = Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'index.html', context={'num_books':num_books,
                                                  'num_instances':num_instances,
                                                  'num_instances_available': num_instances_available,
                                                  'num_authors': num_authors,
                                                  'num_visits': num_visits,
                                                  }
                  )

def index2(request):
    group = Group.objects.all()
    students = group.students_set.all()
    courses = group.course_set.all()
    lecturer = Lecturer.objects.all()
    return render(request, "index2.html", {"group": group, "students": students, "courses": courses})


def add_task(request):
    tasks = Task.objects.all()
    if request.method == "POST":
        form = FormTask(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return redirect('/')
    else:
        form = FormTask()
        return render(request, "add_task.html", {"form": form, "tasks": tasks})

def edit_task(request, task_id):
    tasks = Task.objects.get(id=task_id)
    if request.method == "POST":
        form = FormTask(request.POST, instance=tasks)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = FormTask(instance=tasks)
        return render(request, "edit_task.html", {"form": form, "tasks": tasks})

def delete_task(request, task_id):
    tasks = Task.objects.get(id=task_id)
    if request.method == "POST":
        tasks.delete()
        return redirect('/')
    else:
        return render(request, "delete_task.html", {"tasks": tasks})

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 2