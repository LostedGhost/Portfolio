from django.db import models

# Create your models here.
class Information(models.Model):
    nom_complet = models.CharField(max_length=255, blank=True,  default="")
    nom = models.CharField(max_length=255, blank=True)
    prenom = models.CharField(max_length=255, blank=True)
    profil = models.TextField(blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=255, blank=True)
    a_propos = models.TextField(blank=True)
    localisation = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to="image/", blank=True)
    def __str__(self):
        return f"{self.prenom} {self.nom}"
    
    def competences(self):
        return Competence.objects.all()
    
    def experiences(self):
        return Experience.objects.all().order_by("-date_debut")
    
    def counters(self):
        return Counter.objects.all()
    
    def projets(self):
        return Projet.objects.all()
    
    def messages(self):
        return Message_guess.objects.all().order_by("lu", "-id")
    
    def has_unread_messages(self):
        return Message_guess.objects.filter(lu=False).exists()

class Competence(models.Model):
    nom = models.CharField(max_length=200)
    niveau = models.IntegerField()
    def __str__(self):
        return self.nom
    
class Experience(models.Model):
    titre = models.CharField(max_length=200)
    entreprise = models.CharField(max_length=200)
    description = models.TextField()
    date_debut = models.DateField()
    date_fin = models.DateField(null=True)
    icone = models.CharField(max_length=10)
    def __str__(self):
        return self.titre
    def date_debut_rep(self):
        return self.date_debut.strftime("%Y-%m-%d")
    def date_fin_rep(self):
        if not self.date_fin:
            return ""
        return self.date_fin.strftime("%Y-%m-%d")

class Counter(models.Model):
    nom = models.CharField(max_length=200)
    valeur = models.IntegerField()
    icone = models.CharField(max_length=10, default="bi bi-check")
    def __str__(self):
        return self.nom

class Projet(models.Model):
    titre = models.CharField(max_length=200)
    domaine = models.CharField(max_length=200, default="Développement web")
    date_fin = models.DateField()
    image = models.ImageField(upload_to='images/projets/')
    def __str__(self):
        return self.titre
    
    def date_fin_rep(self):
        return self.date_fin.strftime("%Y-%m-%d")

class Message_guess(models.Model):
    nom = models.CharField(max_length=255)
    email = models.EmailField()
    sujet = models.CharField(max_length=255)
    message = models.TextField()
    lu = models.BooleanField(default=False)
    def __str__(self):
        return self