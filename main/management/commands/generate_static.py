"""
Management command to generate static HTML files for GitHub Pages deployment
"""
import os
from django.core.management.base import BaseCommand
from django.test import Client
from django.conf import settings
from main.models import Project


class Command(BaseCommand):
    help = 'Generate static HTML files for GitHub Pages'

    def handle(self, *args, **options):
        client = Client()
        output_dir = settings.BASE_DIR / 'docs'
        
        # Create output directory
        os.makedirs(output_dir, exist_ok=True)
        os.makedirs(output_dir / 'projects', exist_ok=True)
        
        self.stdout.write('Generating static HTML files...')
        
        # Generate homepage
        self.stdout.write('  - Generating index.html')
        response = client.get('/')
        with open(output_dir / 'index.html', 'w') as f:
            f.write(response.content.decode('utf-8'))
        
        # Generate projects page
        self.stdout.write('  - Generating projects.html')
        response = client.get('/projects/')
        with open(output_dir / 'projects' / 'index.html', 'w') as f:
            f.write(response.content.decode('utf-8'))
        
        # Generate individual project pages
        projects = Project.objects.all()
        for project in projects:
            self.stdout.write(f'  - Generating projects/{project.slug}.html')
            response = client.get(f'/projects/{project.slug}/')
            os.makedirs(output_dir / 'projects' / project.slug, exist_ok=True)
            with open(output_dir / 'projects' / project.slug / 'index.html', 'w') as f:
                f.write(response.content.decode('utf-8'))
        
        # Generate about page
        self.stdout.write('  - Generating about.html')
        response = client.get('/about/')
        os.makedirs(output_dir / 'about', exist_ok=True)
        with open(output_dir / 'about' / 'index.html', 'w') as f:
            f.write(response.content.decode('utf-8'))
        
        # Generate contact page
        self.stdout.write('  - Generating contact.html')
        response = client.get('/contact/')
        os.makedirs(output_dir / 'contact', exist_ok=True)
        with open(output_dir / 'contact' / 'index.html', 'w') as f:
            f.write(response.content.decode('utf-8'))
        
        self.stdout.write(self.style.SUCCESS(f'\nSuccessfully generated static files in {output_dir}'))
        self.stdout.write('\nNote: Static files (CSS, JS, images) need to be collected separately.')
        self.stdout.write('Run: python manage.py collectstatic --noinput')
