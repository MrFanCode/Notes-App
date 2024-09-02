from django.urls import path
from . import views

urlpatterns = [
	path('', views.dashboard, name="dashboard"), # Mapping the dashboard view to the root page
	path('add-notes/', views.add_note, name="add notes"), # Mapping the url for add notes form page 
	path('remove-notes/', views.remove_note, name="remove notes") # Mapping the url for remove notes form page
]