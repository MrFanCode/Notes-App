from django import forms
from .models import Notes


# Add Note Form
class AddNotes(forms.Form):
	# Title field
	title = forms.CharField(
			label="Title",
			max_length=255,
			widget=forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Title',
				'null': 'False'
				})
		) 

	# Note field
	notes = forms.CharField(
			label="Note",
			widget=forms.Textarea(attrs={
				'class':'form-control',
				'placeholder':'Note',
				'null':'False'
				})
		) 



class RemoveNotes(forms.Form):
	# Title field
	title = forms.CharField(
			label="Title",
			max_length=255,
			widget=forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'Title',
				'null':'False'
				})
		)

