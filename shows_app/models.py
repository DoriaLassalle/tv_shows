from django.db import models

# Create your models here.

class Show(models.Model):
    title= models.CharField(max_length=255)
    network=models.CharField(max_length=45)
    release_date=models.DateTimeField(auto_now=False)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Show name: {self.title}"

    def __str__(self):
        return f"Show: {self.title}"