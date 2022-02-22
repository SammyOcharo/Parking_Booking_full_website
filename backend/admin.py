from django.contrib import admin
from .models import PreBook, GetInTouch

# Register your models here.


class PreBookAdmin(admin.ModelAdmin):
    list_display = ('Name','Phone', 'Email', 'Location', 'Parking_Slot', 'Parking_Date')

class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('Name','Email', 'Message')

admin.site.register(PreBook, PreBookAdmin)

admin.site.register(GetInTouch, GetInTouchAdmin)
