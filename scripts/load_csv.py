
import csv

from PartieAdmin.models import *


def run():
    print("import test")

    Etudiant.objects.all().delete()
    Filiere.objects.all().delete()
    Module.objects.all().delete()
    Element.objects.all().delete()
    Departement.objects.all().delete()
    Absence.objects.all().delete()

    with open("input/Etudiant.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        # nom, prenom, filier, module, element, date, heure



        for row in reader:
            print(row)

            etudiant = Etudiant(nom=row[0], prenom=row[1])
            departement = Departement(nom=row[7])
            filiere = Filiere(nom=row[2], departement=departement)
            module = Module(nom=row[3],filiere=filiere)
            element = Element(nom=row[4])
            abscence = Absence(date=row[5], heure=row[6])

            element.module = module
            etudiant.filiere = filiere
            abscence.etudiant = etudiant
            abscence.element = element

            departement.save()
            filiere.save()
            etudiant.save()

            module.save()
            element.save()
            abscence.save()
