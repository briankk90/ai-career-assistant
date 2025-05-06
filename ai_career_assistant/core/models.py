from django.db import models

class UserProfile(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    skills = models.TextField()
    experience = models.TextField()
    preferences = models.TextField()

    def __str__(self):
        return self.user_id

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    company = models.CharField(max_length=200)
    embedding = models.JSONField(null=True)  # Store Pinecone embedding

    def __str__(self):
        return self.title
