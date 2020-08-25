from django.db import models

class TravelEntries(models.Model):
    author_name = models.CharField(max_length=25)
    place_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.place_name

    class Meta:
        verbose_name_plural = "TravelEntries"


    