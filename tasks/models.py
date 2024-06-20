from django.db import models
from autenticacao.models import UserProfile

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Média')
    due_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
