from django.db import models

class BirthdayDate(models.Model):
    date = models.DateTimeField()

    class Meta:
        verbose_name = 'BirthdayDate'
        verbose_name_plural = 'BirthdayDates'

    def __str__(self):
        return str(self.date)


class Image(models.Model):
    image = models.ImageField(upload_to='my-birthday-live-images')
    caption = models.CharField(max_length=200)
    createAt  = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __str__(self):
        return self.caption


class Wish(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    message = models.TextField(max_length=500)
    createAt  = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Wish'
        verbose_name_plural = 'Wishes'


    def __str__(self):
        return self.message