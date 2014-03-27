from django.contrib import admin

from .models import Address, Job, UserPicture

class AddressAdmin(admin.ModelAdmin):
    class Meta:
        model = Address
admin.site.register(Address, AddressAdmin)

class JobAdmin(admin.ModelAdmin):
    class Meta:
        model = Job
admin.site.register(Job, JobAdmin)

class UserPictureAdmin(admin.ModelAdmin):
    class Meta:
        model = UserPicture
admin.site.register(UserPicture, UserPictureAdmin)