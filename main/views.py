from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import (
    Project, Category, Skill, Experience, Education,
    Testimonial, SiteConfiguration
)
from .forms import ContactForm


def index(request):
    """Homepage with hero, featured projects, skills, stats, testimonials"""
    config = SiteConfiguration.get_instance()
    featured_projects = Project.objects.filter(featured=True)[:6]
    skills = Skill.objects.all()
    testimonials = Testimonial.objects.filter(featured=True)
    
    context = {
        'config': config,
        'featured_projects': featured_projects,
        'skills': skills,
        'testimonials': testimonials,
    }
    return render(request, 'main/index.html', context)


def projects(request):
    """Projects page with filtering"""
    category_slug = request.GET.get('category', 'all')
    categories = Category.objects.all()
    
    if category_slug != 'all':
        projects_list = Project.objects.filter(category__slug=category_slug)
    else:
        projects_list = Project.objects.all()
    
    context = {
        'projects': projects_list,
        'categories': categories,
        'active_category': category_slug,
        'config': SiteConfiguration.get_instance(),
    }
    return render(request, 'main/projects.html', context)


def project_detail(request, slug):
    """Individual project page"""
    project = get_object_or_404(Project, slug=slug)
    related_projects = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    
    context = {
        'project': project,
        'related_projects': related_projects,
        'config': SiteConfiguration.get_instance(),
    }
    return render(request, 'main/project_detail.html', context)


def about(request):
    """About page with experience timeline and education"""
    config = SiteConfiguration.get_instance()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    skills = Skill.objects.all()
    
    context = {
        'config': config,
        'experiences': experiences,
        'education': education,
        'skills': skills,
    }
    return render(request, 'main/about.html', context)


def contact(request):
    """Contact page with form"""
    config = SiteConfiguration.get_instance()
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'config': config,
    }
    return render(request, 'main/contact.html', context)

