from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Project, Tag
from .forms import FeedbackForm

# Create your views here.

# projects = [
#     {'name': 'Spelling Bee Mania!', 'image': '', 
#      'technologies': 'HTML, CSS, Javascript', 
#      'description': 'An interactive spelling bee game powered by computer generated voice technology, allowing the user to simulate a realistic spelling bee experience!', 
#      'live': 'https://julibennett.github.io/Project_1_SpellingBee/', 
#      'date': 'January 2024'},
#     {'name': 'NWSL Season Tracker', 'image': '', 'technologies': 'Node.js, Express, EJS, MongoDB, Mongoose, Tailwind CSS', 'description': 'Track all your favorite teams with this tracker app for the National Womens Soccer League. See upcoming games, rosters, and stats all in one easy to use site!', 'live': 'https://nwsl-season-tracker-ef89be7e7b8b.herokuapp.com/sessions/new', 'date': 'March, 2024'},
# ]

def home(request):
  return render(request, 'projects/home.html')

def about(request):
    return render(request, 'projects/about.html')

def projects_index(request):
    projects = Project.objects.all()
    return render(request, 'projects/index.html', {
    'projects': projects
    })

def projects_detail(request, project_id):
   project = Project.objects.get(id=project_id)
   tags = Tag
   id_list = project.tags.all().values_list('id')
   tags_project_doesnt_have = Tag.objects.exclude(id__in=id_list)
   feedback_form = FeedbackForm()
   return render(request, 'projects/detail.html', {
      'project': project,
      'feedback_form': feedback_form,
      'tags': tags_project_doesnt_have,
      })

def add_feedback(request, pk):
   form = FeedbackForm(request.POST)
   if form.is_valid():
      new_feedback = form.save(commit=False)
      new_feedback.project_id = pk
      new_feedback.save()
   return redirect('detail', project_id=pk)

def assoc_tag(request, pk, tag_pk):
   Project.objects.get(id=pk).tags.add(tag_pk)
   return redirect('detail', project_id=pk)

class ProjectCreate(CreateView):
  model = Project
  fields = ['name', 'technologies', 'description', 'live', 'created']

class ProjectUpdate(UpdateView):
  model = Project
  fields = ['technologies', 'description', 'live', 'created']

class ProjectDelete(DeleteView):
  model = Project
  success_url = '/projects'

class TagList(ListView):
  model = Tag

class TagDetail(DetailView):
  model = Tag

class TagCreate(CreateView):
  model = Tag
  fields = '__all__'

class TagUpdate(UpdateView):
  model = Tag
  fields = ['name']

class TagDelete(DeleteView):
  model = Tag
  success_url = '/tags'

