from django.urls import path
from . import views

urlpatterns = [
	path('register/', views.register, name='register'),
	path('login/', views.login, name='login'),
	path('logout/', views.logout, name='logout'),

	# account activate url
	path('activate/', views.activate, name='activate')
]
]
