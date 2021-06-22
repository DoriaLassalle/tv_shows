from django.db import models

# Create your models here.

class Network(models.Model):
    name=models.CharField(max_length=255) 
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    #   shows

    def __repr__(self):
        return f"Network: {self.name}"

    def __str__(self):
        return f"{self.name}"

class Show(models.Model):
    title= models.CharField(max_length=255)
    network=models.ForeignKey(Network, related_name="shows", on_delete=models.CASCADE)
    release_date=models.DateField(auto_now=False)
    description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"Show name: {self.title}"

    def __str__(self):
        return f"Show: {self.title}"

