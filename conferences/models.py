from django.db import models
from django.urls import reverse
from django.utils import timezone

class Conference(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=50, blank=True)
    website = models.URLField(blank=True)
    submission_deadline = models.DateTimeField()
    call_for_papers = models.FileField(
        upload_to='conference_pdfs/',
        blank=True,
        null=True,
        help_text="Upload PDF call for papers"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('conference_detail', kwargs={'pk': self.pk})
    
    def days_until_deadline(self):
        delta = self.submission_deadline - timezone.now()
        return delta.days
    
    def has_call_for_papers(self):
        return bool(self.call_for_papers)