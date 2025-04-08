from django.urls import path
from myapp import views
urlpatterns = [
    path('home/', views.display_home, name='home'),
    path('allarticle/', views.display_allArticles, name='all'),
    path('specarticle/<int:id>', views.display_spec, name='specific'),
]
