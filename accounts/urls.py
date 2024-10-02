from django.urls import path
from . import views 

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    # request에 login된 user의 data가 저장되어 있기 때문에, variable routing을 안 쓴다. ! 
    path('signup/', views.signup, name = 'signup'),
    path('delete/', views.delete, name = 'delete'),
    path('update/', views.update, name = 'update'), 
]
