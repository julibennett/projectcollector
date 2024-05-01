from django.shortcuts import render

# Create your views here.

projects = [
    {'name': 'Spelling Bee Mania!', 'image': '', 
     'technologies': 'HTML, CSS, Javascript', 
     'description': 'An interactive spelling bee game powered by computer generated voice technology, allowing the user to simulate a realistic spelling bee experience!', 
     'live': 'https://julibennett.github.io/Project_1_SpellingBee/', 
     'date': 'January 2024'},
    {'name': 'NWSL Season Tracker', 'image': '', 'technologies': 'Node.js, Express, EJS, MongoDB, Mongoose, Tailwind CSS', 'description': 'Track all your favorite teams with this tracker app for the National Womens Soccer League. See upcoming games, rosters, and stats all in one easy to use site!', 'live': 'https://nwsl-season-tracker-ef89be7e7b8b.herokuapp.com/sessions/new', 'date': 'March, 2024'},
]

def home(request):
  return render(request, 'projects/home.html')

def about(request):
    return render(request, 'projects/about.html')

def projects_index(request):
    # projects = Project.objects.all()
    return render(request, 'projects/index.html', {
    'projects': projects
    })