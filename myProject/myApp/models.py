from django.db import models
from django.utils import timezone

class Task(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Due Today', 'Due Today'),
        ('Overdue', 'Overdue')
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Upcoming')

    def save(self, *args, **kwargs):
        today = timezone.now().date()
        if self.due_date < today:
            self.status = 'Overdue'
        elif self.due_date == today:
            self.status = 'Due Today'
        else:
            self.status = 'Upcoming'
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.title