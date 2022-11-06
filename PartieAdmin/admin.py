from django.contrib import admin

# Register your models here.

from .models import Departement, Filiere, Module, Element, Enseignant, Etudiant, Absence

admin.site.register(Departement)
admin.site.register(Filiere)
admin.site.register(Module)
admin.site.register(Element)
admin.site.register(Enseignant)
admin.site.register(Etudiant)
admin.site.register(Absence)


