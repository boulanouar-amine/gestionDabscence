from django.db import models

# Create your models here.

class Departement(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Filiere(models.Model):
    nom = models.CharField(max_length=100)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Module(models.Model):
    nom = models.CharField(max_length=100)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom

class Element(models.Model):
    nom = models.CharField(max_length=100)
    module = models.ForeignKey(Module, on_delete=models.CASCADE ,related_name='elements')
    def __str__(self):
        return self.nom

class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)

    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    chefdepartement = models.OneToOneField(Departement, on_delete=models.CASCADE, related_name='chefdepartement', null=True, blank=True)

    def __str__(self):
        return self.nom + " " + self.prenom

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    def __str__(self):
        return self.nom + " " + self.prenom


class Absence(models.Model):
    etudiant = models.ForeignKey(Etudiant, on_delete=models.CASCADE)
    element = models.ForeignKey(Element, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField(default='00:00:00')
    def __str__(self):
        return self.etudiant.nom + " " + self.etudiant.prenom + " " + self.element.nom + " " + str(self.date)