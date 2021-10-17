from django.contrib import admin

from .models import Image, BirthdayDate, Wish


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('image',)


@admin.register(BirthdayDate)
class BirthdayDateAdmin(admin.ModelAdmin):
    list_display = ('date',)


@admin.register(Wish)
class WishAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'createAt',  'message')
