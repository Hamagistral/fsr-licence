from django.contrib import admin
from .models import User, Module, FormationLicence, NoteModule, Message, Evenement

# Register your models here.
admin.site.register(User)
admin.site.register(FormationLicence)
admin.site.register(Module)
admin.site.register(Message)
admin.site.register(NoteModule)
admin.site.register(Evenement)