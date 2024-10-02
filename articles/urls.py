from django.urls import path, include
from . import views 

app_name = 'articles'

urlpatterns = [
    
    # 전체 게시글 조회 
    path('', views.index, name='index'), 
    
    # 단일 게시글 조회 (detail 페이지)
    # variable routing 을 
    # 1) 조회 목적으로 사용한다. -> views.py에서 pk 매개변수로 받는다.  
    # 2) url naming pattern 에 pk를 사용한다. 
    path('<int:pk>/', views.detail, name='detail'), 
    
    # 새로운 게시글 만들기. 왜 두 개를 만들어야 할까? 
    # new로 정보를 받을거고(render), create로 DB에 등록한다(redirect)
    path('new/', views.new, name='new'), # 페이지 렌더링 
    path('create/', views.create, name = 'create'), # 페이지 리다이렉트 

    # variable routing : 조회 후 삭제 
    path('<int:pk>/delete', views.delete, name='delete'), 
    
    # variable routing : 조회 후 수정 
    path('<int:pk>/edit', views.edit, name='edit'), # 페이지 렌더링 
    path('<int:pk>/update', views.update, name='update'), # 페이지 리다이렉트 


]
