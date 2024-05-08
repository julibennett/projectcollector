from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('projects/', views.projects_index, name='index'),
    path('projects/<int:project_id>/', views.projects_detail, name='detail'),
    path('projects/create/', views.ProjectCreate.as_view(), name='projects_create'),
    path('projects/<int:pk>/update/', views.ProjectUpdate.as_view(), name='projects_update'),
    path('projects/<int:pk>/delete/', views.ProjectDelete.as_view(), name='projects_delete'),
    path('projects/<int:pk>/add_feedback/', views.add_feedback, name='add_feedback'),
    path('projects/<int:pk>/assoc_tag/<int:tag_pk>/', views.assoc_tag, name='assoc_tag'),

        ## TAG URLS ##
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),

]

