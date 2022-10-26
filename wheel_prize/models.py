from secrets import choice
from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=255 , blank = False, null = False) 
    _start = models.DateTimeField(blank = False, null = False)
    _end = models.DateTimeField(blank = False, null = False)
    description = models.TextField(blank= True)
    
    STATUS_CHOICE = (
        (1 , "Public"),
        (0 , "Private")
    )
    status = models.IntegerField(choices = STATUS_CHOICE , default=1)

    def __str__(self):
        return self.name
    def clean(self):
        if self._start > self._end:
            raise ValidationError(
                {'_start' : 'Invalid Start & End date'}
            )
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)

class EventPrize(models.Model):
    event = models.ForeignKey(Event ,on_delete=models.CASCADE)
    name = models.CharField(max_length = 255  , blank = True)
    prize = models.CharField(max_length=255 , blank = True)
    image = models.ImageField(upload_to='media/event/prize/')

    def __str__(self):
        return str(self.event) + ' | '+ self.name + ' | ' + self.prize 

class PrizeWinPercent(models.Model):
    prize_number = models.IntegerField(blank = False, null = False)
    percent = models.FloatField(blank= False , null = False)
    def __str__(self):
        return str(self.prize_number) + ' | ' + str(self.percent) + '%'
class PrizeLog(models.Model):
    uid = models.TextField(blank = False, null = False)
    prize = models.CharField(max_length=255)
    event = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.uid) + ' | ' + ' | ' + str(self.prize) + ' | ' + str(self.event) 
