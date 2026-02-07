from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Project, Technology, Category, Skill, Experience,
    Education, Testimonial, SiteConfiguration, ContactMessage
)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon_class', 'colored_preview']
    search_fields = ['name']

    def colored_preview(self, obj):
        return format_html(
            '<span style="background-color: {}; padding: 5px 10px; color: white; border-radius: 4px;">{}</span>',
            obj.color, obj.color
        )
    colored_preview.short_description = 'Color'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']


class ProjectTechnologyInline(admin.TabularInline):
    model = Project.technologies.through
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured', 'order', 'created_date']
    list_filter = ['featured', 'category', 'created_date']
    search_fields = ['title', 'short_description', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ['featured', 'order']
    filter_horizontal = ['technologies']
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'short_description', 'description')
        }),
        ('Classification', {
            'fields': ('category', 'technologies')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Links', {
            'fields': ('project_url', 'github_url')
        }),
        ('Display Settings', {
            'fields': ('featured', 'order')
        }),
    )

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('technologies')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency', 'order']
    list_filter = ['category']
    list_editable = ['proficiency', 'order']
    search_fields = ['name']


@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'current', 'order']
    list_filter = ['current']
    list_editable = ['order']
    search_fields = ['company', 'position']
    date_hierarchy = 'start_date'


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['degree', 'institution', 'field_of_study', 'start_date', 'end_date', 'order']
    list_editable = ['order']
    search_fields = ['institution', 'degree', 'field_of_study']
    date_hierarchy = 'start_date'


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'company', 'rating', 'featured', 'order']
    list_filter = ['featured', 'rating']
    list_editable = ['featured', 'order']
    search_fields = ['name', 'position', 'company', 'content']


@admin.register(SiteConfiguration)
class SiteConfigurationAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Basic Information', {
            'fields': ('site_title', 'name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Social Links', {
            'fields': ('github_url', 'linkedin_url', 'twitter_url')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        }),
        ('Statistics', {
            'fields': ('projects_completed', 'years_experience', 'happy_clients', 'technologies_used')
        }),
    )

    def has_add_permission(self, request):
        # Only allow one instance
        return not SiteConfiguration.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Don't allow deletion
        return False


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read']
    list_filter = ['is_read', 'created_at']
    list_editable = ['is_read']
    search_fields = ['name', 'email', 'subject', 'message']
    readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']
    date_hierarchy = 'created_at'

    def has_add_permission(self, request):
        # Messages are created through the contact form only
        return False

