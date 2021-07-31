from django.db import models

class update(models.Model):
    class Meta(object):
        verbose_name = "Telegram update"

    tg_update_id = models.IntegerField(default=None, null=True, blank=True)
    fromid = models.IntegerField(null=True, default=None)
    fromLastName = models.CharField(max_length=100)
    fromFirstName = models.CharField(max_length=100)
    date = models.DateTimeField(null=True, default=None)
    text = models.CharField(max_length=10000)
    def __str__(self):
        return "{} {} {} {}".format(self.date, self.fromid, self.fromFirstName, self.fromLastName)

