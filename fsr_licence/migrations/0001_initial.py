# Generated by Django 3.2.9 on 2024-04-28 13:46

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_quill.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('role', models.CharField(choices=[('ETUDIANT', 'Etudiant'), ('PROFESSEUR', 'Professeur')], default='ETUDIANT', max_length=24)),
                ('cin', models.TextField(default='-')),
                ('massar', models.TextField(blank=True)),
                ('birthdate', models.DateField(default=django.utils.timezone.now)),
                ('nationality', models.TextField(default='Marocain')),
                ('address', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='FormationLicence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('presentation', models.TextField()),
                ('mode', models.CharField(choices=[('Initiale', 'Initiale'), ('Continue', 'Continue')], default='Initiale', max_length=24)),
                ('type', models.CharField(choices=[('Fondamentale', 'Fondamentale'), ('Education', 'Education'), ('Professionelle', 'Professionelle'), ('Excellence', 'Excellence')], default='Fondamentale', max_length=32)),
                ('categorie', models.CharField(choices=[('Mathématiques', 'Mathématiques'), ('Informatique', 'Informatique'), ('Géologie', 'Géologie'), ('Chimie', 'Chimie'), ('Physique', 'Physique')], default='-', max_length=32)),
                ('cursus', models.TextField(blank=True, null=True)),
                ('prerequis', models.TextField(blank=True, null=True)),
                ('debouches', models.TextField(blank=True, null=True)),
                ('capacity', models.IntegerField(default=300)),
                ('lien_fiche_pdf', models.URLField(blank=True)),
                ('responsable', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('etudiants', models.ManyToManyField(limit_choices_to={'role': 'ETUDIANT'}, null=True, related_name='etudiant_modules', to=settings.AUTH_USER_MODEL)),
                ('formation_licence', models.ManyToManyField(null=True, to='fsr_licence.FormationLicence')),
                ('professeur', models.ForeignKey(limit_choices_to={'role': 'PROFESSEUR'}, on_delete=django.db.models.deletion.CASCADE, related_name='professeur_modules', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NoteModule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valeur', models.FloatField()),
                ('etudiant', models.ForeignKey(limit_choices_to={'role': 'ETUDIANT'}, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fsr_licence.module')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=56)),
                ('title', models.CharField(max_length=56)),
                ('body', django_quill.fields.QuillField(blank=True, null=True)),
                ('cue', models.CharField(max_length=500, null=True)),
                ('summary', models.CharField(max_length=1000, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255)),
                ('message_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver_messages', to=settings.AUTH_USER_MODEL)),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender_messages', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('esubject', models.CharField(max_length=56)),
                ('date', models.DateField()),
                ('details', models.CharField(max_length=56, null=True)),
                ('theme', models.CharField(max_length=24, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('heure', models.TimeField()),
                ('lieu', models.CharField(max_length=255)),
                ('formation_licence', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='fsr_licence.formationlicence')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='formation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='fsr_licence.formationlicence'),
        ),
        migrations.AddField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
