
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('pickle_app.urls')),  # Include your app URLs under the 'api/' path
]
