from django.db import models
from django.utils.text import slugify

class Project(models.Model):
    title = models.CharField(max_length=100)
    # blank=True allows the admin to leave it empty; the save() method will fill it
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField()
    # This matches the 'p.tech' used in your HTML loop
    technologies = models.CharField(
        max_length=200, 
        default="Python, Django", 
        help_text="e.g. React, Tailwind, Python"
    )
    github_link = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Document(models.Model):
    """
    Used for the VS Code editor files. 
    To show a 'README', create a document with the slug 'readme'.
    """
    title = models.CharField(max_length=100) 
    content = models.TextField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    """
    Optional: If you want to list specific code snippets 
    inside your terminal or editor.
    """
    name = models.CharField(max_length=100)
    extension = models.CharField(max_length=10, default=".py")
    content = models.TextField(blank=True)
    updated_at = models.DateTimeField(auto_now=True)   

    def __str__(self):
        return f"{self.name}{self.extension}"