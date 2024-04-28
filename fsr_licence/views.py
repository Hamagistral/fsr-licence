from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import User, FormationLicence, NoteModule, Module, Message, Evenement
from .forms import formation, module, message_form
from django.db.models import Count

def index(request):
    return render(request, "fsr_licence/index.html")
    
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("dashboard"))
        else:
            return render(request, "fsr_licence/login.html", {
                "message": "Nom d'utilisateur et / ou mot de passe incorrect."
            })
    else:
        return render(request, "fsr_licence/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        role = request.POST["role"]
        cin = request.POST["cin"]
        massar = request.POST["massar"]
        birthdate = request.POST["birthdate"]
        address = request.POST["address"]
        nationality = request.POST["nationality"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "fsr_licence/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.role = role
            user.first_name = first_name
            user.last_name = last_name
            user.cin = cin
            user.massar = massar
            user.birthdate = birthdate
            user.nationality = nationality
            user.address = address
            user.save()
        except IntegrityError:
            return render(request, "fsr_licence/register.html", {
                "message": "Username already taken."
            })
        
        login(request, user)
        return HttpResponseRedirect(reverse("dashboard"))
    else:
        return render(request, "fsr_licence/register.html")

def presentation_view(request):
    return render(request, "fsr_licence/presentation.html")

def formations_view(request):
    return render(request, "fsr_licence/formations.html")

def formations_licence(request):
    return render(request, "fsr_licence/formation_licence.html")

@login_required
def dashboard_view(request):
    # Get the count of users with role "ETUDIANT"
    etudiants_count = User.objects.filter(role='ETUDIANT').count()
    professeurs_count = User.objects.filter(role='PROFESSEUR').count()
    formations_count = FormationLicence.objects.count()
    modules_count = Module.objects.count()

    messages = Message.objects.filter(receiver=request.user).order_by('-created_at')

    return render(request, "fsr_licence/dashboard.html", {
        'etudiants_count': etudiants_count,
        'professeurs_count': professeurs_count,
        'formations_count': formations_count,
        'modules_count': modules_count,
        'messages': messages
    })

@login_required
def profile_view(request):
    return render(request, "fsr_licence/profile.html")


@login_required
def message_view(request, id):
    message = Message.objects.get(id=id)
    
    return render(request, "fsr_licence/message_view.html", {"message": message})

@login_required
def new_message(request):
    if request.method == "POST":
        newMessage = message_form(request.POST)

        if newMessage.is_valid():
            sender = request.user
            receiver = newMessage.cleaned_data['receiver']
            subject = newMessage.cleaned_data['subject']
            message_text = newMessage.cleaned_data['message_text']

            nMessage = Message(sender=sender, receiver=receiver, subject=subject, message_text=message_text)
            nMessage.save()

            return redirect(reverse("dashboard"))
        else:
            newMessage.errors.as_data()
            return render(request, "fsr_licence/new_message.html", {'form': message_form})

    elif request.method == "GET":
        return render(request, "fsr_licence/new_message.html", {'form': message_form})

@login_required
def reply_message(request, id):
    message = Message.objects.get(id=id)
    subject = f"Re: {message.subject}"
    
    if request.method == "POST":
        newMessage = message_form(request.POST)

        if newMessage.is_valid():
            sender = request.user
            receiver = newMessage.cleaned_data['receiver']
            subject = subject
            message_text = newMessage.cleaned_data['message_text']

            nMessage = Message(sender=sender, receiver=receiver, subject=subject, message_text=message_text)
            nMessage.save()

            return redirect(reverse("dashboard"))
        else:
            print(newMessage.errors.as_data())

            return render(request, "fsr_licence/reply_message.html", {'form': message_form, 'message': message})

    elif request.method == "GET":
        return render(request, "fsr_licence/reply_message.html", {'form': message_form, 'message': message})

@login_required
def formations_admin(request):
    formations = FormationLicence.objects.annotate(
      etudiant_count=Count('user__formation'),  # Filter students
      modules_count=Count('module__formation_licence')
    ).all()
    
    return render(request, "fsr_licence/formations_admin.html", {"formations": formations})

@login_required
def add_formation(request):
    if request.method == "POST":
        user = request.user
        newFormation = formation(request.POST)

        if newFormation.is_valid():
            nom = newFormation.cleaned_data['nom']
            presentation = newFormation.cleaned_data['presentation']
            type = newFormation.cleaned_data['type']
            responsable = newFormation.cleaned_data['responsable']
            cursus = newFormation.cleaned_data['cursus']
            prerequis = newFormation.cleaned_data['prerequis']
            capacity = newFormation.cleaned_data['capacity']
            debouches = newFormation.cleaned_data['debouches']
            lien_fiche_pdf = newFormation.cleaned_data['lien_fiche_pdf']

            nFormation = FormationLicence(nom=nom, presentation=presentation, type=type, responsable=responsable, cursus=cursus, prerequis=prerequis, debouches=debouches, capacity=capacity, lien_fiche_pdf=lien_fiche_pdf)
            nFormation.save()

            return redirect(reverse("formations_admin"))
        else:
            return render(request, "fsr_licence/add_formation.html", {"form": formation})

    elif request.method == "GET":
        return render(request, "fsr_licence/add_formation.html", {"form": formation})

def view_formation(request, id):
    formation = FormationLicence.objects.get(id=id)

    return render(request, "fsr_licence/formation_details.html", {"formation": formation})

def view_formations_cat(request, cat):
    formations = FormationLicence.objects.filter(categorie=cat)

    return render(request, "fsr_licence/formations_cat.html", {"formations": formations})

@login_required    
def edit_formation(request, id):
    formationUpdate = FormationLicence.objects.get(id=id)
    form = formation(instance=formationUpdate)

    if request.method == "POST":
        # Pre-populate form with existing content
        form = formation(request.POST, instance=formationUpdate)

        if form.is_valid():
            form.save()

            return redirect(reverse('view_formation', args=[formationUpdate.id]))
        
        else:
            print(form.errors.as_data())

    return render(request, "fsr_licence/edit_formation.html", {'form': form, 'id': id})

@login_required    
def delete_formation(request, id):
    FormationLicence.objects.filter(id=id).delete()

    return redirect(reverse("formations_admin"))

@login_required
def modules_admin(request):
    modules = Module.objects.all()
    
    return render(request, "fsr_licence/modules_admin.html", {"modules": modules})

@login_required
def add_module(request):
    if request.method == "POST":
        user = request.user
        newModule = module(request.POST)

        if newModule.is_valid():
            nom = newModule.cleaned_data['nom']
            description = newModule.cleaned_data['description']
            professeur = newModule.cleaned_data['professeur']
            formation = newModule.cleaned_data['formation']

            nModule = Module(nom=nom, description=description, professeur=professeur, formation_licence=formation)
            nModule.save()

            return redirect(reverse("modules_admin"))
        else:
            return render(request, "fsr_licence/add_module.html", {"form": module})

    elif request.method == "GET":
        return render(request, "fsr_licence/add_module.html", {"form": module})
    
@login_required 
def view_module(request, id):
    module = Module.objects.get(id=id)
    etudiants = module.etudiants.all()
    notes = NoteModule.objects.filter(module=module)

    return render(request, "fsr_licence/module_details.html", {"module": module, "etudiants": etudiants, "notes": notes})    

@login_required    
def edit_module(request, id):
    moduleUpdate = Module.objects.get(id=id)
    form = module(instance=moduleUpdate)

    if request.method == "POST":
        # Pre-populate form with existing content
        form = module(request.POST, instance=moduleUpdate)

        if form.is_valid():
            form.save()

            return redirect(reverse('view_module', args=[moduleUpdate.id]))
        
        else:
            print(form.errors.as_data())

    return render(request, "fsr_licence/edit_module.html", {'form': form, 'id': id})

@login_required    
def delete_module(request, id):
    Module.objects.filter(id=id).delete()

    return redirect(reverse("modules_admin"))

@login_required
def etudiants_admin(request):
    etudiants = User.objects.filter(role="ETUDIANT")
    
    return render(request, "fsr_licence/etudiants_admin.html", {"etudiants": etudiants})

@login_required
def professeurs_admin(request):
    professeurs = User.objects.filter(role="PROFESSEUR")
    formations = FormationLicence.objects.all()
    
    return render(request, "fsr_licence/professeurs_admin.html", {"professeurs": professeurs, 'formations': formations})

@login_required
def evenements_admin(request):
    evenements = Evenement.objects.all()
    
    return render(request, "fsr_licence/evenements_admin.html", {"evenements": evenements})

@login_required
def view_notes(request):
    modules = Module.objects.filter(etudiants=request.user)
    notes_module = NoteModule.objects.filter(etudiant=request.user)
    print(notes_module)
    return render(request, "fsr_licence/notes_etudiant.html", {"modules": modules, "notes": notes_module})