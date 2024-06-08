from django.db import models

# Create your models here.


class Usersearch(models.Model):
    messages_box = models.CharField(max_length=100)


    def __str__(self) -> str:
        return self.messages_box

    class Meta:
        ordering = ['messages_box']
        verbose_name = 'messages'