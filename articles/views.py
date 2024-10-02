from django.shortcuts import render, redirect

# Create your views here.
# 현재 디렉토리의 models.py에서 Article 모델을 가져오겠다. 
from .models import Article

def index(request): 
  # QuerySet API : 전체 데이터 조회 
  articles = Article.objects.all() 

  context = { 
    'articles' : articles
  }

  return render(request, 'articles/index.html', context)

# 단일 게시글 페이지 렌더링(조회) 
def detail(request, pk): # 매개변수로 pk도 받는다. url에 variable routing을 사용했으니까 
  # QuerySet API 가 단일 데이터 조회에 사용된다. (all 말고, get)
  # 단일 게시글 조회라 s를 제외한 article 로 받겠다. 
  article = Article.objects.get(pk=pk) # 뒤의 pk는 매개변수로 받은 pk. 앞의 pk는 인자
  context = {
    'article' : article, 
  }
  return render(request, 'articles/detail.html', context)

# index()와 detail()은 모두 QuerySetAPI가 사용되었지만, 
# index는 전체 데이터 조회라 .all() 메서드가 사용되었고, 
# detail은 단일 데이터 조회라 .get() 메서드가 사용되었다. 

def new(request): 
  return render(request, 'articles/new.html') 


# 페이지 리다이렉트, 데이터를 받아서 DB에 저장하기 때문에 GET 아니고 POST 방식   
  # GET 방식은 데이터가 url에 노출 -> 데이터를 조회, 검색할 때 사용 
  # POST 방식은 보안성이 좋아 -> 데이터를 생성, 수정, 삭제할 때 사용 (CSRF 토큰 활용)
# render와 redirect의 차이 
  # render : 사용자에게 새로운 페이지를 보여줄 때 사용 
  # redirect : 데이터 처리 후 다른 페이지로 이동하려 할 때 사용 
  # 게시글을 생성했다 하고, 이 작업이 끝나면 어떤 페이지로 이동할건가? 생각하면 redirect, render 구분할 수 있다. 

def create(request): 
  title = request.POST.get('title')
  content = request.POST.get('content')

  # 2번 저장법 - 코드가 간결하면서 안정성도 있다(save를 나중에 하니까)
  article = Article(title = title, content = content)
  # save 하기 전, 유효성 검사를 하기 때문에 안정성 검사를 이 줄에서 한다. 
  article.save()

  # 데이터를 변경하고 나면 
  # 클라이언트가 GET 요청을 한 번 더 보내도록 한다 (redirect)
  # 데이터가 변경되었을 때 경로에 요청 
  return redirect('articles:detail', article.pk)   

def delete(request, pk): 
  article = Article.objects.get(pk=pk) 
  article.delete() 
  return redirect('articles:index')

# create와 차이 ? 
# 기존에 있던 게시글 조회하는지/조회하지 않는지 
def edit(request, pk): 
  article = Article.objects.get(pk=pk) 
  context = {
    'article' : article 
  }
  return render(request, 'articles/edit.html', context)

def update(request, pk): 
  article = Article.objects.get(pk=pk) 
  article.title = request.POST.get('title')
  article.content = request.POST.get('content')
  article.save()

  return redirect('articles:detail', article.pk)