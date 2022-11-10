import csv

from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.http import HttpResponse

# Register your models here.

from .models import Departement, Filiere, Module, Element, Enseignant, Etudiant, Absence

class AbsenceAdmin(admin.ModelAdmin):
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response



    export_as_csv.short_description = "Export Selected"
    actions = ("export_as_csv",)


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Departement)
admin.site.register(Filiere)
admin.site.register(Module)
admin.site.register(Element)
admin.site.register(Enseignant)
admin.site.register(Etudiant)


admin.site.site_header = "Partie Admin"

admin.site.register(Absence,AbsenceAdmin)