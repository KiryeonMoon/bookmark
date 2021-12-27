from django.contrib import admin

# Register your models here.
# 내가 만든 모델(데이터베이스)을 관리자(admin) 페이지에서 관리할 수 있도록, 모델을 등록하는 .py파일

from .models import Bookmark  # 현재 패키지(폴더) 속 models라는 모듈에서 Bookmark 모듈을 불러오겠다.

# Bookmark 모델 등록
# 아래 코드가 있느냐 없느냐에 따라 서버 admin 페이지에서 Bookmark 타이틀이 나타나고 안나타나고가 결정됨
admin.site.register(Bookmark)
