from django.db import models


class LogApiRequestsModel(models.Model):
    """
    For storing logged information about request to database
    """
    user = models.CharField(max_length=256, verbose_name="Username")
    url = models.CharField(max_length=256, verbose_name="Request sent to URL")
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        date_time = self.time.strftime("%d.%m.%y %H:%M:%S")
        return f"{date_time}: User `{self.user}` made request to {self.url}"
