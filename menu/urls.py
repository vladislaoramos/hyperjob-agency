from django.urls import path
from .views import MainView, MyLoginView, SignUpView, HomeView
from django.views.generic import RedirectView

urlpatterns = [
    path('', MainView.as_view(), name='home-page'),
    path('login', MyLoginView.as_view(), name='login-page'),
    path('login/', RedirectView.as_view(url='/login')),
    path('signup', SignUpView.as_view(), name='sign-up'),
    path('signup/', RedirectView.as_view(url='/signup')),
    path('home', HomeView.as_view(), name='profile'),
]
