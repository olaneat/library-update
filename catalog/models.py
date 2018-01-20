from django.urls import reverse
from django.db import models
import uuid
# Create your models here.
class Genre(models.Model):
	"""
	models representation of the book genre
	"""
	name = models.CharField(max_length = 200, help_text = "enter the book genre of the book (e.g scientify, adventure, fiction )")
	def __str__(self):
		"""
		string for representing the model object(in admit sites)
		"""
		return self.name

class Book(models.Model):
	"""
	A representation of a book (not a copy of the book)
	"""
	tittle = models.CharField(max_length = 200)
	author = models.ForeignKey('Author', on_delete = models.SET_NULL, null = True)
	summary = models.TextField(max_length = 1000, help_text = 'Enter a description of the book here ')
	isbn = models.CharField('ISBN', max_length =13, help_text = '13 character < a href = "https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
	genre = models.ManyToManyField(Genre, help_text = "Enter the book genre here ")

	def __str__(self):
		"""
		string representation of the object
		"""
		return self.tittle


	def get_absolute_url(self):
		"""
		return the url access to a book
		"""
		return reverse('book-detail', args =[str(self.id)])

	def display_genre(self):
		"""
		displaying a list for the genre
		"""
		return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
	display_genre.short_description = 'Genre'



class BookInstance(models.Model):
	"""
	model representing a specify copy of a 	book
	"""
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, help_text = 'unique ID for the book')
	book = models.ForeignKey('Book', on_delete = models.SET_NULL, null = True)
	imprint = models.CharField(max_length = 200)
	due_date = models.DateField(null = True, blank = True)


	LOAN_STATUS = (
		('m', 'Maintance'),
		('o', 'on_loan' ),
		('a', 'Available'),
		('r', 'reserved'),
		)
	status = models.CharField(max_length = 1, choices = LOAN_STATUS, blank = True, default = 'm', help_text = 'Available books')
class Meta:
	odering = ["due_back"]


def __str__(self):
	"""
	string for representing the object
	"""
	return '%s (%s)' %(self.id,self.book.tittle)

class Author(models.Model):
	"""
	representation of the object models 
	"""
	first_name = models.CharField(max_length = 100)
	last_name = models.CharField(max_length = 100)
	DOB = models.DateField(null = True, blank = True)
	DOD = models.DateField('died', null = True, blank = True )

	
	def __str__(self):
			"""
			string representing the object models
			"""
			return '%s, %s' %(self.last_name, self.first_name)
class Language(models.Model):
	"""
	representation of the Language models
	"""
	language = models.TextField(max_length = 100, help_text = "input the language of the book here")


	def __str__(self):

		"""
		string representing the object models
		"""
		return self.language

	