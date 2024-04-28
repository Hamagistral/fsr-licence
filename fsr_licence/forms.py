from django import forms
from .models import User, FormationLicence, Module, Message

type_choices = [('Fondamentale', 'Fondamentale'), ('Education', 'Education'), ('Professionelle', 'Professionelle'), ('Excellence', 'Excellence')]
mode_choices = [('Initiale', 'Initiale'), ('Continue', 'Continue')]

class formation(forms.ModelForm):
    nom = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Nom", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "56", "spellcheck": "false", "required": "false"}))
    presentation = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Presentation", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false", "required": "false"}))
    mode = forms.CharField(label="", widget=forms.Select(choices=mode_choices, attrs={"placeholder": "Mode", "autocomplete": "off", "class": "px-2 h-9 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "required": "false"}))
    type = forms.CharField(label="", widget=forms.Select(choices=type_choices, attrs={"placeholder": "Tye", "autocomplete": "off", "class": "px-2 h-9 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "required": "false"}))
    responsable = forms.ModelChoiceField(queryset=User.objects.filter(role='PROFESSEUR'), label="", widget=forms.Select(attrs={"placeholder": "Responsable", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    cursus = forms.CharField(label="", required = False, widget=forms.Textarea(attrs={"required": "False", "placeholder": "Cursus", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false", "required": "false"}))
    prerequis = forms.CharField(label="", required = False, widget=forms.Textarea(attrs={"placeholder": "Prerequis", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false"}))
    debouches = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Débouchés", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false", "required": "false"}))
    capacity = forms.IntegerField(label="", widget=forms.TextInput(attrs={"placeholder": "Capacité d'acceuil", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false", "required": "false"}))
    lien_fiche_pdf = forms.URLField(label="", widget=forms.TextInput(attrs={"placeholder": "Lien Fiche PDF", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false", "required": "false"}))
    
    class Meta:
        model = FormationLicence

        fields = [
            "nom",
            "presentation",
            "mode",
            "type",
            "responsable",
            "cursus",
            "prerequis",
            "debouches",
            "capacity",
            "lien_fiche_pdf"
        ]

class module(forms.ModelForm):
    nom = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Nom", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "56", "spellcheck": "false"}))
    description = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Description", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    professeur = forms.ModelChoiceField(queryset=User.objects.filter(role='PROFESSEUR'), label="", widget=forms.Select(attrs={"placeholder": "Professeur", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    etudiants = forms.ModelMultipleChoiceField(queryset=User.objects.filter(role='ETUDIANT'), label="", widget=forms.SelectMultiple(attrs={"placeholder": "Etudiants", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    formation = forms.ModelMultipleChoiceField(queryset=FormationLicence.objects, label="", widget=forms.SelectMultiple(attrs={"placeholder": "Formation Licence", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    
    class Meta:
        model = Module

        fields = [
            "nom",
            "description",
            "professeur",
            "formation",
        ]

class message_form(forms.ModelForm):
    receiver = forms.ModelChoiceField(queryset=User.objects.all(), label="", widget=forms.Select(attrs={"placeholder": "Destinataire", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Sujet", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "spellcheck": "false"}))
    message_text = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Message", "autocomplete": "off", "class": "px-2 block w-full rounded-md border-0 py-1.5 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-400 sm:text-sm sm:leading-6", "maxlength": "1000", "spellcheck": "false", "required": "false"}))

    class Meta:
        model = Message
        fields = ['receiver', 'subject', 'message_text']