from django.db import models


class PIN(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, default='13')
    pin_number = models.IntegerField(default=13)
    state = models.BooleanField(default=0)

    def __str__(self):
        return self.name