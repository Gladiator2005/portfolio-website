from django.db import models
from django.utils.text import slugify

# Create your models here.

class Technology(models.Model):
    name = models.CharField(max_length=100)
    icon_class = models.CharField(max_length=100, blank=True, help_text="Font Awesome class (e.g., fa-brands fa-python)")
    color = models.CharField(max_length=7, default='#6366f1', help_text="Hex color code")

    class Meta:
        verbose_name_plural = "Technologies"
        ordering = ['name']

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    short_description = models.CharField(max_length=300)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    technologies = models.ManyToManyField(Technology, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    project_url = models.URLField(blank=True, help_text="Live project URL")
    github_url = models.URLField(blank=True, help_text="GitHub repository URL")
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0, help_text="Display order (lower numbers appear first)")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['order', '-created_date']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('frontend', 'Frontend'),
        ('backend', 'Backend'),
        ('devops', 'DevOps'),
        ('tools', 'Tools'),
        ('other', 'Other'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, default='other')
    proficiency = models.IntegerField(default=80, help_text="0-100")
    icon_class = models.CharField(max_length=100, blank=True, help_text="Font Awesome class")
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return f"{self.name} ({self.category})"


class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True, help_text="Leave blank if current")
    description = models.TextField()
    current = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

    @property
    def duration(self):
        from datetime import date
        end = self.end_date if self.end_date else date.today()
        delta = end - self.start_date
        years = delta.days // 365
        months = (delta.days % 365) // 30
        if years > 0:
            return f"{years} year{'s' if years > 1 else ''} {months} month{'s' if months != 1 else ''}"
        return f"{months} month{'s' if months != 1 else ''}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    field_of_study = models.CharField(max_length=200, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    description = models.TextField(blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-start_date']

    def __str__(self):
        return f"{self.degree} - {self.institution}"


class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating = models.IntegerField(default=5, help_text="1-5 stars")
    featured = models.BooleanField(default=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.name} - {self.position}"


class SiteConfiguration(models.Model):
    site_title = models.CharField(max_length=200, default='Portfolio')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200, help_text="Job title / tagline")
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/', blank=True, null=True)
    resume_file = models.FileField(upload_to='resume/', blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)
    location = models.CharField(max_length=200, blank=True)
    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    
    # Stats for the counter section
    projects_completed = models.IntegerField(default=0)
    years_experience = models.IntegerField(default=0)
    happy_clients = models.IntegerField(default=0)
    technologies_used = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"

    def __str__(self):
        return f"Site Configuration - {self.name}"

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and SiteConfiguration.objects.exists():
            raise ValueError('There can only be one SiteConfiguration instance')
        super().save(*args, **kwargs)

    @classmethod
    def get_instance(cls):
        """Get or create the singleton instance"""
        instance, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'name': 'Your Name',
                'title': 'Full Stack Developer',
                'bio': 'Welcome to my portfolio!',
                'email': 'contact@example.com',
            }
        )
        return instance


class ContactMessage(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=300)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.subject}"

