#from PartieAdmin.models import *
import csv


def run():
    with open('../input/Etudiant.csv') as file:
        reader = csv.reader(file)
        next(reader)  # Advance past the header
        # nom, prenom, filier, module, element, date, heure

        # Etudiant.objects.all().delete()
        # Filiere.objects.all().delete()
        print("test")
        for row in reader:

            print(row)

            # Etudiant
            #
            # Element = Element(name=row[0])
            # film.save()