from django.db import models

class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50)
    type_p = models.CharField(max_length=50)
    producer = models.CharField(max_length=50)
    amount = models.IntegerField()

    def __str__(self):
        return(f"{self.name}")