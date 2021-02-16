from django.db import models

# Create your models here.
class Certificate(models.Model):
    Event_Name = models.TextField(max_length=50)
    image = models.ImageField(upload_to='certificates/')

    def __str__(self):
        return str(self.Event_Name)


class ParticipantData(models.Model):
    Full_Name = models.TextField(max_length=50)
    Event_Name = models.ForeignKey(to=Certificate, on_delete=models.PROTECT, related_name="eventsname")
    Description = models.TextField(max_length=200)

    def __str__(self):
        return str(self.Full_Name)



