from django.db import models
from django.db.models import fields
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView  # 클래스 뷰 : 상속받아 사용한다고 생각
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bookmark
'''
view : 기능을 담당(페이지 단위)
화면이 나타나는 view, 화면이 없는 view
화면이 있건 없건 주소 url은 있어야 한다.

view 내용(함수, 클래스)과 url이 있으면 동작한다.

view의 코드 형식 : 함수형 or 클래스형
 - 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수
            내가 원하는대로 동작들을 설계하고 만들고 싶을 때
- 클래스형 : CRUD, 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
            상속하여 받아 사용한다.

장고는 장고의 제네릭 view를 많이 사용함
'''

# url을 입력 -> 웹서버가 그 url에 해당되는 뷰를 찾아서 동작시킨다 -> 응답(우리가 그 화면을 봄)
# (중요) 여기 view.py에서 웹서버가 응답해줄 view를 만드는거고, 이 view가 동작하기 위해 사용자가 입력해야 하는 url은 url.py에 따로 만들어줘야 한다.

# [CRUD]


# Read
class BookmarkListView(ListView):
    model = Bookmark  # 클래스형 view는 어떤 모델에 관해 다룰 것인지에 대해 무조건 코드가 작성되어야 함


# Create
class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']  # 해당 모델에 있는 field들 중 입력&수정할 field가 어떤 것인지 지정
    success_url = reverse_lazy(
        "list"
    )  # 입력이 성공했을 때 이동할 url 지정, reverse_lazy : url 패턴 이름을 가지고 url을 만들어주는 기능
    template_name_suffix = "_create"


# Read
class BookmarkDetailView(DetailView):
    model = Bookmark


# Update
class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = "_update"


# Delete
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy("list")  # 삭제가 성공했을 때 어디론가 가야 하니까 필요
