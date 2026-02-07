from django_distill import distill_path
from main import views
from main.models import Project

def get_all_project_slugs():
    """Get all project slugs for static generation"""
    return [p.slug for p in Project.objects.all()]

urlpatterns = [
    distill_path('', views.index, name='index'),
    distill_path('projects/', views.projects, name='projects'),
    distill_path('about/', views.about, name='about'),
    distill_path('contact/', views.contact, name='contact'),
    distill_path(
        'projects/<slug:slug>/',
        views.project_detail,
        name='project_detail',
        distill_func=get_all_project_slugs,
        distill_file='projects/{param_0}.html'
    ),
]
