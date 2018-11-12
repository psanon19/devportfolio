from django.contrib import admin

from .models import FormModel,ContactMeModel, WildCardModel

admin.site.register(FormModel)
admin.site.register(ContactMeModel)
admin.site.register(WildCardModel)