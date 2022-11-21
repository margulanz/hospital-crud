from django.contrib import admin
from .models import Country, Discover, Disease, Diseasetype, Doctor, Publicservant, Record,Specialize,Users



# Register your models here.
admin.site.register(Country)
admin.site.register(Discover)
admin.site.register(Diseasetype)
admin.site.register(Disease)
admin.site.register(Doctor)
admin.site.register(Publicservant)
admin.site.register(Record)
admin.site.register(Specialize)
admin.site.register(Users)
