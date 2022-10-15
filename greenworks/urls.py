from django.contrib import admin
from django.urls import path, include
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='/accounts/login')),
    path('accounts/', include('django.contrib.auth.urls')),

    path('admin/', admin.site.urls),
    path('__debug__/', include('debug_toolbar.urls')),

    path('dashboard/', views.dashboard, name='dashboard'),
    path('sales/', include('sales.urls')),
    path('expenses/', include('expenses.urls')),

    # path('manager/', include('manager.urls')),
    path('weather/', include('weather.urls')),


]
