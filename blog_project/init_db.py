import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog_project.settings')
django.setup()

from django.core.management import call_command

if __name__ == "__main__":
    call_command('migrate')