from django.db import models

# Create your models here.

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    processed_file = models.FileField(upload_to='processed/', null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
