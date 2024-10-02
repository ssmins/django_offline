from django.db import models

# Create your models here.

# AbstractUser : 로그인, 권한 관리 등에 필요한 기본적인 필드 제공 ! -> 설계도 파일 보면 다양하게 있다. 
from django.contrib.auth.models import AbstractUser

class User(AbstractUser): 
    pass 