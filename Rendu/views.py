from django.shortcuts import render, redirect
from Rendu.models import *
from datetime import datetime

# Create your views here.
def handle404(request, exception):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.filter(password=password)
    return render(request, 'error/404.html', {
        "infos": infos,
        "error": error,
        "success": success,
    })

def handle500(request):
    return render(request, 'error/500.html')

def index(request):
    success = request.session.pop("success", None)
    error = request.session.pop("error", None)
    all = Information.objects.all().first()
    if request.POST:
        try:
            nom = request.POST.get("name", None)
            email = request.POST.get("email", None)
            sujet = request.POST.get("subject", None)
            message = request.POST.get("message", None)
            message_guess = Message_guess(nom=nom,  email=email, sujet=sujet, message=message)
            message_guess.save()
        except:
            request.session["error"] = "Votre message n'a pas pu être envoyé"
            return redirect("/#contact")
        request.session["success"] = "Votre message a été envoyé avec succès"
        return redirect("/#contact")
    return render(request, "index.html",{
        "success": success,
        "error": error,
        "me": all,
    })

def login(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        return redirect("/my_dash")
    if request.POST:
        password = request.POST.get("password", None)
        if Information.objects.filter(password=password).exists():
            request.session["password"] = password
            return redirect("/my_dash")
        else:
            request.session["error"] = "Mot de passe incorrect"
            return redirect("/login")
    return render(request, "Load/login.html",{
        "error": error,
        "success": success,
    })

def logout(request):
    request.session.clear()
    return redirect("/")

def my_dash(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/index.html", {
        "infos": infos,
        "error": error,
        "success": success,
    })

def infos(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        infos.nom_complet = request.POST.get("nom_complet", None)
        infos.nom = request.POST.get("nom", None)
        infos.prenom = request.POST.get("prenom", None)
        infos.profil = request.POST.get("profil", None)
        infos.email = request.POST.get("email", None)
        infos.telephone = request.POST.get("telephone", None)
        infos.a_propos = request.POST.get("a_propos", None)
        infos.localisation = request.POST.get("localisation", None)
        if request.POST.get("password", None)!= None and request.POST.get("re-password", None)== request.POST.get("password", None):
            infos.password = request.POST.get("password", None)
            request.session["password"] = infos.password
            infos.save()
            request.session["success"] = "Vos informations ont été modifiées avec succès"
        else:
            request.session["error"] = "Les deux mots de passe ne sont pas identiques"
        return redirect("/infos")
    return render(request, "Load/infos.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def competences(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/competences.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def competence_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        try:
            competence = Competence(nom=request.POST.get("nom", None), niveau=request.POST.get("niveau", None))
            competence.save()
            request.session["success"] = "Votre compétence a bien été ajoutée"
        except:
            request.session["error"] = "Votre compétence n'a pas pu être ajoutée"
        return redirect("/competences")
    return render(request, "Load/competence_add.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def competence_delete(request, id):
    competence = Competence.objects.get(id=id)
    competence.delete()
    request.session["success"] = "Votre compétence a bien été supprimée"
    return redirect("/competences")

def competence_edit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    competence = Competence.objects.get(id=id)
    if request.POST:
        try:
            competence.nom = request.POST.get("nom", None)
            competence.niveau = request.POST.get("niveau", None)
            competence.save()
            request.session["success"] = "Votre compétence a bien été modifiée"
        except:
            request.session["error"] = "Votre compétence n'a pas pu être modifiée"
        return redirect("/competences")
    return render(request, "Load/competence_edit.html",{
        "infos": infos,
        "comp": competence,
        "error": error,
        "success": success,
    })

def experiences(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/experiences.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def experience_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        try:
            experience = Experience(titre=request.POST.get("titre", None), entreprise=request.POST.get("entreprise", None).upper(), date_debut=request.POST.get("date_debut", None), date_fin=request.POST.get("date_fin",None), description=request.POST.get("description", None), icone=request.POST.get("icone", None))
            experience.save()
            request.session["success"] = "Votre expérience a bien été ajoutée"
        except:
            request.session["error"] = "Votre expérience n'a pas pu être ajoutée"
        return redirect("/experiences")
    return render(request, "Load/experience_add.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def experience_delete(request, id):
    experience = Experience.objects.get(id=id)
    experience.delete()
    request.session["success"] = "Votre expérience a bien été supprimée"
    return redirect("/experiences")

def experience_edit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    experience = Experience.objects.get(id=id)
    if request.POST:
        try:
            experience.titre = request.POST.get("titre", None)
            experience.entreprise = request.POST.get("entreprise", None).upper()
            experience.date_debut = request.POST.get("date_debut", None)
            experience.date_fin = request.POST.get("date_fin", None)
            experience.description = request.POST.get("description", None)
            experience.icone = request.POST.get("icone", None)
            experience.save()
            request.session["success"] = "Votre expérience a bien été modifiée"
        except:
            request.session["error"] = "Votre expérience n'a pas pu être modifiée"
        return redirect("/experiences")
    return render(request, "Load/experience_edit.html",{
        "infos": infos,
        "exp": experience,
        "error": error,
        "success": success,
    })

def counters(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/counters.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def counter_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        try:
            counter = Counter(nom=request.POST.get("nom", None).upper(), valeur=request.POST.get("valeur", None), icone=request.POST.get("icone", None))
            counter.save()
            request.session["success"] = "Votre compteur a bien été ajouté"
        except:
            request.session["error"] = "Votre compteur n'a pas pu être ajouté"
        return redirect("/counters")
    return render(request, "Load/counter_add.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def counter_edit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    counter = Counter.objects.get(id=id)
    if request.POST:
        try:
            counter.nom = request.POST.get("nom", None).upper()
            counter.valeur = request.POST.get("valeur", None)
            counter.icone = request.POST.get("icone", None)
            counter.save()
            request.session["success"] = "Votre compteur a bien été modifié"
        except:
            request.session["error"] = "Votre compteur n'a pas pu être modifié"
        return redirect("/counters")
    return render(request, "Load/counter_edit.html",{
            "infos": infos,
            "count": counter,
            "error": error,
            "success": success,
        })

def counter_delete(request, id):
    counter = Counter.objects.get(id=id)
    counter.delete()
    request.session["success"] = "Votre compteur a bien été supprimé"
    return redirect("/counters")

def projets(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/projets.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def projet_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        try:
            projet = Projet(titre=request.POST.get("titre", None).upper(), domaine=request.POST.get("domaine", None), date_fin=request.POST.get("date_fin", None), image=request.FILES["image"])
            projet.save()
            request.session["success"] = "Votre projet a bien été ajouté"
        except:
            request.session["error"] = "Votre projet n'a pas pu être ajouté"
        return redirect("/projets")
    return render(request, "Load/projet_add.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def projet_edit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    projet = Projet.objects.get(id=id)
    if request.POST:
        try:
            projet.titre = request.POST.get("titre", None).upper()
            projet.domaine = request.POST.get("domaine", None)
            projet.date_fin = request.POST.get("date_fin", None)
            img = request.FILES["image"]
            if img:
                projet.image = img
            projet.save()
            request.session["success"] = "Votre projet a bien été modifié"
        except:
            request.session["error"] = "Votre projet n'a pas pu être modifié"
        return redirect("/projets")
    return render(request, "Load/projet_edit.html",{
            "infos": infos,
            "pro": projet,
            "error": error,
            "success": success,
        })

def projet_delete(request, id):
    projet = Projet.objects.get(id=id)
    projet.delete()
    request.session["success"] = "Votre projet a bien été supprimé"
    return redirect("/projets")

def messages(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/messages.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def message_read(request, id):
    message = Message_guess.objects.get(id=id)
    message.lu = True
    message.save()
    request.session["success"] = "Votre message a bien été lu"
    return redirect("/messages_guess")

def techs(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    return render(request, "Load/techs.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def tech_add(request):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    if request.POST:
        try:
            tech = Technology(nom=request.POST.get("nom", None).upper(), image=request.FILES["image"])
            tech.save()
            request.session["success"] = "Votre technologie a bien été ajoutée"
        except:
            request.session["error"] = "Votre technologie n'a pas pu être ajoutée"
        return redirect("/techs")
    return render(request, "Load/tech_add.html",{
        "infos": infos,
        "error": error,
        "success": success,
    })

def tech_edit(request, id):
    error = request.session.pop("error", None)
    success = request.session.pop("success", None)
    password = request.session.get("password", None)
    if password and Information.objects.filter(password=password).exists():
        pass
    else:
        return redirect("/login")
    infos = Information.objects.get(password=password)
    tech = Technology.objects.get(id=id)
    if request.POST:
        try:
            tech.nom = request.POST.get("nom", None).upper()
            img = request.FILES.get("image", None)
            if img:
                tech.image = img
            tech.save()
            request.session["success"] = "Votre technologie a bien été modifiée"
        except:
            request.session["error"] = "Votre technologie n'a pas pu être modifiée"
        return redirect("/techs")
    return render(request, "Load/tech_edit.html",{
            "infos": infos,
            "tech": tech,
            "error": error,
            "success": success,
        })

def tech_delete(request, id):
    tech = Technology.objects.get(id=id)
    tech.delete()
    request.session["success"] = "Votre technologie a bien été supprimé"
    return redirect("/techs")
