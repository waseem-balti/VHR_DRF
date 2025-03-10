from django.db import models
from django.contrib.auth.models import User

class Position(models.Model):

    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
    
class Applicant(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Selected', 'Selected'),
        ('Rejected', 'Rejected'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applicants", null=True, blank=True)
    fullname = models.CharField(max_length=255)
    email = models.EmailField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE, related_name="applicants")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('email', 'position')

    def __str__(self):
        return self.fullname
    
class Question(models.Model):
    text = models.TextField()
    positions = models.ManyToManyField(Position, related_name="questions")
    time_limit = models.IntegerField(default=60)  # Time limit in seconds

    def __str__(self):
        return self.text[:50]

class ApplicantResponse(models.Model):
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE, related_name="responses")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name="responses")
    video_response = models.FileField(upload_to='videos/', null=True, blank=True)
    submission_time = models.DateTimeField(auto_now_add=True)
    score = models.IntegerField(null=True, blank=True) 
    def __str__(self):
        return f"{self.applicant.fullname} - {self.question.text[:30]}"


class Interview(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    scheduled_date = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
    candidate_name = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return self.title