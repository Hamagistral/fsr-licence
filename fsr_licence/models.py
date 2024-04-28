from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

# Modèles pour les formations licences
class FormationLicence(models.Model):
    MODE = (
        ('Initiale', 'Initiale'),
        ('Continue', 'Continue'),
    )

    TYPE = (
        ('Fondamentale', 'Fondamentale'),
        ('Education', 'Education'),
        ('Professionelle', 'Professionelle'),
        ('Excellence', 'Excellence'),
    )
    
    CATEGORIE = (
        ('Mathématiques', 'Mathématiques'),
        ('Informatique', 'Informatique'),
        ('Géologie', 'Géologie'),
        ('Chimie', 'Chimie'),
        ('Physique', 'Physique')
    )

    nom = models.CharField(max_length=255)
    presentation = models.TextField()
    mode = models.CharField(max_length=24, choices=MODE, default='Initiale')
    type = models.CharField(max_length=32, choices=TYPE, default='Fondamentale')
    categorie = models.CharField(max_length=32, choices=CATEGORIE, default='-')
    responsable = models.ForeignKey('User', on_delete=models.SET_NULL, blank=True, null=True)
    cursus = models.TextField(blank=True, null=True)
    prerequis = models.TextField(blank=True, null=True)
    debouches = models.TextField(blank=True, null=True)
    capacity = models.IntegerField(default=300)
    lien_fiche_pdf = models.URLField(blank=True)

    def __str__(self):
        return self.nom

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ETUDIANT', 'Etudiant'),
        ('PROFESSEUR', 'Professeur'),
    )

    role = models.CharField(max_length=24, choices=ROLE_CHOICES, default='ETUDIANT')
    cin = models.TextField(blank=False, default="-")
    massar = models.TextField(blank=True)
    birthdate = models.DateField(blank=False, default=timezone.now)
    nationality = models.TextField(blank=False, default="Marocain")
    address = models.TextField(blank=True)
    formation = models.ForeignKey(FormationLicence, on_delete=models.SET_NULL, blank=True, null=True)

# Modèles pour les messages
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver_messages')
    subject = models.CharField(max_length=255)
    message_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"From: {self.sender.username} To: {self.receiver.username} - {self.subject[:20]}"

# Modèles pour les modules
class Module(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    professeur = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'PROFESSEUR'}, related_name='professeur_modules')
    etudiants = models.ManyToManyField(User, limit_choices_to={'role': 'ETUDIANT'}, related_name='etudiant_modules', null=True)
    formation_licence = models.ManyToManyField(FormationLicence, null=True)

    def __str__(self):
        return self.nom
    
# Modèles pour les événements
class Evenement(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=255)
    formation_licence = models.ForeignKey(FormationLicence, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.titre

# Modèles pour les notes
class NoteModule(models.Model):
    valeur = models.FloatField()
    etudiant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'ETUDIANT'}, null=True)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.etudiant} - {self.module.nom}: {self.valeur}"
 