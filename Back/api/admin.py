from django.contrib import admin
from .models import Medcin , Patient , Administratif , User ,Infirmier , Laborantin , Radiologue,Consultation,Soin,DPI,Ordonnance,Resume,Bilan
# Register your models here.

admin.site.register(Medcin )
admin.site.register(Patient)
admin.site.register(Administratif)
admin.site.register(User)
admin.site.register(Infirmier)
admin.site.register(Laborantin)
admin.site.register(Radiologue)
admin.site.register( Consultation)
admin.site.register( Soin)
admin.site.register( DPI)
admin.site.register( Resume)
admin.site.register( Bilan)
admin.site.register( Ordonnance)
