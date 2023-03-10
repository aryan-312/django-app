from django.db import models

# Create your models here.
class Note(models.Model):
    owners = models.ForeignKey('auth.User', related_name='notes', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    heading = models.CharField(max_length=100, blank=True, default='Insert Heading')
    content = models.CharField(max_length=1000, blank=True, default='Write your Note...')

    class Meta:
        ordering = ["created"]

