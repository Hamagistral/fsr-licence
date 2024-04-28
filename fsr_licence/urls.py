from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("formations", views.formations_view, name="formations"),
    path("presentation", views.presentation_view, name="presentation"),

    path("dashboard", views.dashboard_view, name="dashboard"),
    path("profile", views.profile_view, name="profile"),

    path("message/<int:id>", views.message_view, name="message_view"),
    path("nouveau_message", views.new_message, name="new_message"),
    path("repondre_message/<int:id>", views.reply_message, name="reply_message"),
    
    path("formation_licence", views.formations_licence, name="formation_licence"),
    path("formation", views.formations_admin, name="formations_admin"),
    path("formation/<int:id>", views.view_formation, name="view_formation"),
    path("formation/edit/<int:id>", views.edit_formation, name="edit_formation"),
    path("formation/add", views.add_formation, name="add_formation"),
    path("formation/delete/<int:id>", views.delete_formation, name="delete_formation"),

    path("formations/<str:cat>", views.view_formations_cat, name="view_formations_cat"),
            
    path("modules", views.modules_admin, name="modules_admin"),
    path("module/add", views.add_module, name="add_module"),
    path("module/<int:id>", views.view_module, name="view_module"),
    path("module/edit/<int:id>", views.edit_module, name="edit_module"),
    path("module/delete/<int:id>", views.delete_module, name="delete_module"),

    path("evenements", views.evenements_admin, name="evenements_admin"),
    path("notes", views.view_notes, name="view_notes"),

    path("etudiants", views.etudiants_admin, name="etudiants_admin"),
    path("professeurs", views.professeurs_admin, name="professeurs_admin"),
]