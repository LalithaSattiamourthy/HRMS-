from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('hr.urls')),  # Replace 'api.urls' with your actual API URL configuration
    # Add a path for the root URL
    path('', include('hr.urls')),  # Replace 'your_app.urls' with your app's URL configuration
]
