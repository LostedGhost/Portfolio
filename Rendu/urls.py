from django.urls import path
from Rendu import views

urlpatterns = [
    path(r'', views.index, name="home"),
    path(r'my_dash', views.my_dash, name="my_dash"),
    path(r'infos', views.infos, name="infos"),
    path(r'login', views.login, name="login"),
    path(r'logout', views.logout, name="login"),
    
    path(r'competences', views.competences, name="competences"),
    path(r'competence_add', views.competence_add, name="competence_add"),
    path(r'competence_delete/<int:id>', views.competence_delete, name="competence_delete"),
    path(r'competence_edit/<int:id>', views.competence_edit, name="competence_edit"),
    
    path(r'experiences', views.experiences, name="experiences"),
    path(r'experience_add', views.experience_add, name="experience_add"),
    path(r'experience_delete/<int:id>', views.experience_delete, name="experience_delete"),
    path(r'experience_edit/<int:id>', views.experience_edit, name="experience_edit"),
    
    path(r'counters', views.counters, name="counters"),
    path(r'counter_add', views.counter_add, name="counter_add"),
    path(r'counter_delete/<int:id>', views.counter_delete, name="counter_delete"),
    path(r'counter_edit/<int:id>', views.counter_edit, name="counter_edit"),
    
    path(r'projets', views.projets, name="projets"),
    path(r'projet_add', views.projet_add, name="projet_add"),
    path(r'projet_edit/<int:id>', views.projet_edit, name="projet_edit"),
    path(r'projet_delete/<int:id>', views.projet_delete, name="projet_delete"),
    
    path(r'techs', views.techs, name="techs"),
    path(r'tech_add', views.tech_add, name="tech_add"),
    path(r'tech_edit/<int:id>', views.tech_edit, name="tech_edit"),
    path(r'tech_delete/<int:id>', views.tech_delete, name="tech_delete"),
    
    path(r'messages_guess', views.messages, name="messages"),
    path(r'message_read/<int:id>', views.message_read, name="message_read"),
    
]