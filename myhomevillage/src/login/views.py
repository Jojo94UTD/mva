

from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection

from django.contrib.auth import login
from django.contrib.auth.models import User  # Pour créer un utilisateur de la session si nécessaire
from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection

def loginreg(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, mot_de_passe FROM utilisateur WHERE username = %s OR email = %s",
                           [username, username])
            row = cursor.fetchone()

            if row is None:
                messages.error(request, "Nom d'utilisateur ou email incorrect.")
                return redirect('login-register')

            user_id, hashed_password = row

            if check_password(password, hashed_password):
                #messages.success(request, "Connexion réussie !")

                # Créer une session manuellement
                request.session['user_id'] = user_id
                request.session['username'] = username

                return redirect('navigate-index')  # Redirige vers la page d'accueil après la connexion
            else:
                messages.error(request, "Mot de passe incorrect.")
                return redirect('login-register')

    return render(request, 'login_register.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Les mots de passe ne correspondent pas.")
            return redirect('login-register')

        with connection.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM utilisateur WHERE username = %s", [username])
            if cursor.fetchone()[0] > 0:
                messages.error(request, "Le nom d'utilisateur existe déjà.")
                return redirect('login-register')

            cursor.execute("SELECT COUNT(*) FROM utilisateur WHERE email = %s", [email])
            if cursor.fetchone()[0] > 0:
                messages.error(request, "L'adresse email est déjà utilisée.")
                return redirect('login-register')

            hashed_password = make_password(password1)

            cursor.execute(
                "INSERT INTO utilisateur (username, email, mot_de_passe) VALUES (%s, %s, %s)",
                [username, email, hashed_password]
            )

        messages.success(request, f"Compte créé pour {username} !")
        return redirect('login-register')

    return render(request, 'login_register.html')




