from django.contrib import admin

# Register your models here.
INSTALLED_APPS = [
    # Other installed apps...
    'studentapp',  # Replace 'your_app_name' with the actual name of your app.
]

from django.contrib import admin
from .models import Details  # Import your model here

admin.site.register(Details)  # Register your model with the admin site
