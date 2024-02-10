from django.db import models










class Specialty(models.Model):
    Name=models.CharField(max_length=40,unique=True)
    class Meta:
          def __str__(self):
              return self.Name