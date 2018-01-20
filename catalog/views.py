from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic
# Create your views here.

def index(request):
	"""
	a views representation of the home page
	"""
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	#a
	num_instance_available = BookInstance.objects.filter(status__exact = 'a').count()
	num_author = Author.objects.count()

	return render(
		request, 
		'index.html',
		context = {'num_books': num_books, 'num_instances': num_instances, 'num_instance_available': num_instance_available, 'num_author':num_author})

class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book