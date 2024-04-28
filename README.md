# 👨‍🎓 Site Web: Gestion des Licences de la FSR

Ce projet développe une application web pour la gestion des formations de licence à la Faculté des Sciences Rénovées (FSR) de l'Université Mohammed V de Rabat. L'application permet aux étudiants, aux enseignants et aux administrateurs d'accéder à des informations sur les formations, de gérer les candidatures et les inscriptions, de suivre la progression des étudiants, et de communiquer entre eux.


![homepage](https://i.ibb.co/Dr0YTQ5/image.png)

### 🛠️ Technologies utilisées

- **Back End:** Django
- **Front End:** HTML, TailwindCSS
- **Base de données:** SQLite

### 🔎 Fonctionnalités principales

#### Pour les utilisateurs normaux:

- **Consultation du Panier des Formations :** Accès à des informations détaillées sur les différentes filières de licence, cursus, modules proposés, prérequis, débouchés professionnels, téléchargement de fiche PDF.
- **Candidature et Inscription à la Formation :** Formulaire de candidature en ligne, suivi de la candidature, notifications par email.
- **Accès aux Archives de la Formation :** Liste des lauréats, activités et workshops organisés, agenda des événements à venir, noms des anciens lauréats.

####  Pour les utilisateurs identifiés (Étudiants):

- **Consultation des Cours, TD, TPs, et Résultats :** Plan de cours, supports de cours, résultats détaillés, évolution des résultats au fil du semestre.
- **Accès aux Archives des Lauréats Précédents :** Informations plus complètes sur les lauréats (adresse e-mail, expérience professionnelle, conseils et témoignages).
- **Possibilité de Contacter les Professeurs ou l'Administration :** Formulaire de contact, messagerie interne.

####  Pour les Professeurs et Administrateurs:

- **Gestion d'Événements, Étudiants, Notes, Cours, et Informations sur les Étudiants :** Ajout, modification et suppression d'événements, gestion des étudiants inscrits, gestion des notes, gestion des informations sur les étudiants.
- **Possibilité de Contacter les Étudiants :** Envoi de messages aux étudiants individuellement ou par groupe.
Installation

![acceuil](https://i.ibb.co/s2LYkXZ/image.png)
![catalogue](https://i.ibb.co/cwHgScn/image.png)
![footer](https://i.ibb.co/kQF7pxH/image.png)
![formation](https://i.ibb.co/L5gNrWx/image.png)
![etudiants](https://i.ibb.co/wh5cn4k/image.png)
![professeurs](https://i.ibb.co/Y26jMQQ/image.png)
![formations](https://i.ibb.co/W6YBg9R/image.png)
![modules](https://i.ibb.co/3mtWWjT/image.png)
![events](https://i.ibb.co/VVrF3wx/image.png)
![moduledetail](https://i.ibb.co/mJz2MdX/image.png)
![account](https://i.ibb.co/FJ75KL3/image.png)

### 🔌 Installation

1. Cloner le dépôt:

```shell
git clone https://github.com/Hamagistral/fsr-licence.git
```

2. Créer un environnement virtuel et activer:
```shell
python3 -m venv venv
source venv/bin/activate
```

3. Installer les dépendances:

```shell
pip install -r requirements.txt
```

4. Configurer la base de données:

```shell
python manage.py makemigrations
python manage.py migrate
```

5. Démarrer le serveur de développement:

```shell
python manage.py runserver
```

> L'application sera accessible à l'adresse http://localhost:8000.

