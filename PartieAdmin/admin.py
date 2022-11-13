import csv

from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.http import HttpResponse

# Register your models here.

from .models import Departement, Filiere, Module, Element, Enseignant, Etudiant, Absence

class AbsenceAdmin(admin.ModelAdmin):

    list_filter = ( 'element__module__filiere', 'element__module','element')
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


class ModuleInline(admin.TabularInline):
    model = Module
    extra = 1

class ElementInline(admin.TabularInline):
    model = Element
    extra = 1

class FiliereInline(admin.TabularInline):
    model = Filiere
    extra = 1
class ModuleAdmin(admin.ModelAdmin):
    inlines = [ElementInline]
    list_display = ('nom', 'filiere')



class FiliereAdmin(admin.ModelAdmin):
    inlines = [ModuleInline]
    list_display = ('nom', 'departement')



class DepartementAdmin(admin.ModelAdmin):
    inlines = [FiliereInline]
    extra = 1


admin.site.site_header = "Partie Admin"

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(Departement, DepartementAdmin)
admin.site.register(Filiere,FiliereAdmin)
admin.site.register(Module,ModuleAdmin)
admin.site.register(Absence,AbsenceAdmin)

admin.site.register(Element)
admin.site.register(Enseignant)
admin.site.register(Etudiant)



