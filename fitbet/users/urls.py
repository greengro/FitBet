from users.views import dashboard
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r"^dashboard/", dashboard, name="dashboard"),
    path('accounts/', include('django.contrib.auth.urls')),
]