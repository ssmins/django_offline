# django auth 폼에서 유저 생성 폼, 유저 변경 폼 가져오기 
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 

'''
# 직접 참조 : 
from .models import User

class CustomUserCreationForm(UserCreationForm): 
    class Meta(UserCreationForm.Meta): 
        model = User 
'''

# 간접 참조 :  
from django.contrib.auth import get_user_model 

# 생성 
class CustomUserCreationForm(UserCreationForm): 
    class Meta(UserCreationForm.Meta): 
        model = get_user_model() 

# 변경 
class CustomUserChangeForm(UserChangeForm): 
    class Meta(UserChangeForm): 
        model = get_user_model() 
        fields = ('first_name', 'last_name', 'email', ) # 어떤 회원정보를 변경할건지 
