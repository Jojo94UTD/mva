from django.db import models

class Region(models.Model):
    nomRegion = models.CharField(max_length=100)
    chefLieu = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table ='region'

    def __str__(self):
        return self.nomRegion

from django.db import models

class Ville(models.Model):
    idVille = models.AutoField(primary_key=True)
    nomVille = models.CharField(max_length=100)
    nomLangue = models.CharField(max_length=100)
    nomGardienLangue = models.CharField(max_length=100)
    prenomGardienLangue = models.CharField(max_length=100)
    numTelGardien = models.CharField(max_length=20)
    mailGardien = models.EmailField(max_length=255, blank=True, null=True)
    nomSecretaire = models.CharField(max_length=100, blank=True, null=True)
    prenomSecretaire = models.CharField(max_length=100, blank=True, null=True)
    numTelSecretaire = models.CharField(max_length=20, blank=True, null=True)
    mailSecretaire = models.EmailField(max_length=255, blank=True, null=True)
    photoGardienPath = models.ImageField(upload_to='imagesChefferies/gardienFoto/', null=True, blank=True)
    photoSecretairePath = models.CharField(max_length=255, blank=True, null=True)
    qualite = models.CharField(max_length=255, blank=True, null=True)  # Nouveau champ
    source = models.BooleanField(null=True)  # Nouveau champ (binaire)

    class Meta:
        db_table = 'ville'  # Nom de la table dans la base de données


    def __str__(self):
        return self.nomVille
