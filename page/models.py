from django.db import models

# Create your models here.
class Designer(models.Model):
    image = models.ImageField(upload_to = 'images/')
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 255)
    description = models.TextField()
    # 디자이너 이름 표시 
    def __str__(self):
        return self.name