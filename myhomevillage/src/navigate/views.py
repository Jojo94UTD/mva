
from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import Ville  # Assurez-vous que le modèle Region est défini
import os
from django.conf import settings
from django.contrib import messages


def repertoire(request):
    villes = Ville.objects.all()
    return render(request, 'repertoire.html', {'villes': villes})
def index_nav(request):
    return render(request, "nav_index.html")

def ville_detail(request, idVille):
    ville = get_object_or_404(Ville, idVille=idVille)
    return render(request, 'ville.html', {'ville': ville})

from django.shortcuts import render, get_object_or_404, redirect
from django.db import connection
from .models import Ville
import os
from django.conf import settings

def contribuer(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_ville = request.POST.get('nomVille')
        nom_langue = request.POST.get('nomLangue')
        nom_gardien_langue = request.POST.get('nomGardienLangue')
        prenom_gardien_langue = request.POST.get('prenomGardienLangue')
        num_tel_gardien = request.POST.get('numTelGardien')
        mail_gardien = request.POST.get('mailGardien')
        nom_secretaire = request.POST.get('nomSecretaire')
        prenom_secretaire = request.POST.get('prenomSecretaire')
        num_tel_secretaire = request.POST.get('numTelSecretaire')
        mail_secretaire = request.POST.get('mailSecretaire')
        qualite = request.POST.get('qualite')
        source = 1

        # Gestion de l'image du gardien
        photo_gardien_path = None
        if 'photoGardien' in request.FILES and request.FILES['photoGardien']:
            photo_gardien = request.FILES['photoGardien']
            # Définir le chemin du fichier à stocker
            photo_gardien_path = os.path.join('imagesChefferies', photo_gardien.name)
            # Sauvegarder l'image dans le dossier static
            static_path = os.path.join(settings.BASE_DIR, 'static', 'imagesChefferies')
            if not os.path.exists(static_path):
                os.makedirs(static_path)
            # Vérifier si le fichier est bien enregistré
            file_path = os.path.join(static_path, photo_gardien.name)
            with open(file_path, 'wb+') as destination:
                for chunk in photo_gardien.chunks():
                    destination.write(chunk)
            print(f"Image sauvegardée à : {file_path}")  # Debug print pour vérifier

        # Insertion dans la base de données avec le curseur
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO ville 
                    (nomVille, nomLangue, nomGardienLangue, prenomGardienLangue, numTelGardien, mailGardien, 
                    nomSecretaire, prenomSecretaire, numTelSecretaire, mailSecretaire, qualite, source, photoGardienPath)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                """, [
                    nom_ville, nom_langue, nom_gardien_langue, prenom_gardien_langue,
                    num_tel_gardien, mail_gardien, nom_secretaire,
                    prenom_secretaire, num_tel_secretaire, mail_secretaire,
                    qualite, source, photo_gardien_path  # Ajout de la qualité et source
                ])
            print(f"Data inserted successfully")
            return redirect('remerciement')
        except Exception as e:
            print(f"An error occurred: {e}")  # Debug print pour vérifier les erreurs

        # Redirection après soumission
          # Redirige vers la même page (ou changez la redirection si nécessaire)

    return render(request, 'contribuer.html')


def avis(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire
        nom_utilisateur = request.POST.get('nomUtilisateur')
        prenom_utilisateur = request.POST.get('prenomUtilisateur')
        mail = request.POST.get('mail')
        commentaire = request.POST.get('commentaire')

        # Insertion dans la base de données
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO avis (nomUtilisateur, prenomUtilisateur, mail, commentaire)
                    VALUES (%s, %s, %s, %s)
                """, [nom_utilisateur, prenom_utilisateur, mail, commentaire])
            # Ajout d'un message de succès
            messages.success(request, 'Votre avis a été envoyé avec succès !')
        except Exception as e:
            messages.error(request, 'Une erreur est survenue lors de l\'envoi de votre avis.')

        # Redirection après soumission pour éviter le double envoi du formulaire
        return redirect('avis')

    return render(request, 'avis.html')

def remerciement(request):
    return render(request, 'remerciement.html')

def carte(request):
    return render(request, 'carte.html')




