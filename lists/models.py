from django.db import models

# Create your models here.

class Entry(models.Model):
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return 'Entry'.format(self.id)

    class Meta:
        verbose_name_plural = 'lists'
