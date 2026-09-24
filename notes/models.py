# notes/models.py
from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):

    CATEGORY_CHOICES = [
        ('personal', 'Personal'),
        ('work', 'Work'),
        ('study', 'Study'),
        ('health', 'Health'),
        ('finance', 'Finance'),
        ('other', 'Other'),
    ]

    TAG_CHOICES = [
        ('important', 'Important'),
        ('urgent', 'Urgent'),
        ('idea', 'Idea'),
        ('todo', 'Todo'),
        ('reminder', 'Reminder'),
        ('reference', 'Reference'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='other')
    tag = models.CharField(max_length=50, choices=TAG_CHOICES, default='important')
    is_pinned = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-is_pinned', '-updated_at']

    def __str__(self):
        return f"{self.user.username} - {self.title}"