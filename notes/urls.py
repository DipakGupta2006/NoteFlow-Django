from django.urls import path
from . import views


app_name = 'notes'

urlpatterns = [
    path("create/", views.note_create, name="note_create"),
    path("list/", views.note_list, name="note_list"),
    path('<int:pk>/', views.note_detail, name='note_detail'),
    path('<int:pk>/edit/', views.note_edit, name='note_edit'),
    path('<int:pk>/delete/', views.note_delete, name='note_delete'),
    path("archive/<int:pk>/", views.note_archive, name="note_archive"),
    path("archived-notes/", views.note_archive_list, name="note_archive_list"),
    path("unarchive/<int:pk>/", views.note_unarchive, name="note_unarchive"),

]