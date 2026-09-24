from django import forms
from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content', 'category', 'tag', 'is_pinned']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Note ka title likho...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 6,
                'placeholder': 'Note likho...'
            }),
            'category': forms.Select(attrs={
                'class': 'form-select'
            }),
            'tag': forms.Select(attrs={
                'class': 'form-select'
            }),
            'is_pinned': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }
        labels = {
            'title': 'Title',
            'content': 'Content',
            'category': 'Category',
            'tag': 'Tag',
            'is_pinned': 'Pin this note?',
        }