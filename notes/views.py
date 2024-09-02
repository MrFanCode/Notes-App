from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect


# Getting the current date with date module
from datetime import datetime

# Loading in Forms and Database
from .models import Notes
from .form import AddNotes, RemoveNotes


# Dashboard view with all notes from database listed
def dashboard(request):
	template = loader.get_template('dashboard.html')
	notes = Notes.objects.all().values() # Getting all values from the database
	context = {}
	context['notes'] = notes # Loading the data into the page
	return HttpResponse(template.render(context, request))



# Add note view with a form to add notes
def add_note(request):
	template = loader.get_template('add_note.html')
	context = {}
	form = AddNotes() # Initializing form
	
	# Handle the form
	if request.method == "POST":
		form = AddNotes(request.POST)
		if form.is_valid(): # Validate form input
			title = form.cleaned_data['title'] # Fetching the title from the form
			db = Notes.objects.filter(title=title).values()
			# Validate that title is not already in the database
			if len(db) == 0:
				notes = form.cleaned_data['notes'] # Fetching the notes from the form
				date_added = datetime.today() # Adding the current date when adding the note to database

				# Adding to database
				note = Notes(title=title,notes=notes,date_added=date_added) # Getting the data and filling the database
				note.save() # Finally saving the data into database

				return redirect('dashboard') # Redirect user to dashboard where all notes are listed.
			elif len(db) == 1:
				return HttpResponse("<h1>Notes on this title is already exist.</h1>")

	context['form'] = form
	return HttpResponse(template.render(context, request))



# Remove note page with a notes delete form
def remove_note(request):
	template = loader.get_template('remove_note.html')
	context = {}
	form = RemoveNotes()

	# Handle then form
	if request.method == "POST":
		form = RemoveNotes(request.POST)
		if form.is_valid():
			title = form.cleaned_data['title']

			db = Notes.objects.filter(title=title).values()
			# Validate that title is not already in the database
			if len(db) == 0:
				return HttpResponse("The title is not exist in the database.")
			elif len(db) == 1:
				note = Notes.objects.filter(title=title)
				note.delete()
				return redirect('dashboard')

	context['form'] = form
	return HttpResponse(template.render(context, request))



