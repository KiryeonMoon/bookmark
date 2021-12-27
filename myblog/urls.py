"""
웹프로그래밍 : 홈페이지 만들기, 웹서비스 만들기
FrontEnd : 화면(웹브라우저에서 동작하는 코드) - HTML, CSS, JS
BackEnd : 서버(데이터 입출력 or 계산, 서버에서 동작)
  => 컴퓨터에서 동작하는 언어(Python, Ruby, Java, PHP, JS, C#)
  => GO, Erlang, Perl

- 웹사이트 동작 방식
 => 웹 브라우저 주소창에 url 입력 후 엔터
 => url을 이용하여 서버 ip를 찾는다.
 => ip를 이용해서 서버에 접속
 => url에 해당하는 자료를 요청
 => 웹 어플리케이션이 url을 해석해서 해당하는 코드가 동작
 => 코드의 동작 결과를 응답으로 돌려줌
 => 서버가 웹브라우저로 데이터를 보내줌
 => 웹 브라우저 응답받은 데이터를 화면에 표시

- 백엔드 코드 : 각 url 패턴마다 소스코드 1개 이상

Framework : 어떤 일을 할 때 자주 사용되는 기능을 미리 준비해둔 것
 => 제품을 빨리 출시해야 된다.
 - Micro : 최소한의 기능만 가지고 있다 + 추가 기능을 원하는대로 설치해서 사용한다. Flask
 - FullStack : 거의 대부분의 기능을 갖고 있다 + 추가 기능도 설치 가능. Django

디자인 패턴 : 개발 설계상 발생하는 문제를 해결하기 위한 해결책(디자이너, 프론트엔드, 백엔드)
- MVC : Model(데이터베이스), View(화면-프론트), Controller(계산, 처리-백엔드)
- MTV : Model(데이터베이스), Template(화면-프론트), View(계산, 처리-벡엔드)

장고로 프로젝트 만드는 순서
1. IDE 켜기
2. 장고 설치
3. 장고 프로젝트 만들기
4. 설정하기(데이터베이스, S3)
5. 데이터베이스 초기화
6. 관리자 계정 만들기

<한 프로젝트 진행과정에서 하기 순서 계속 반복>
7. 앱 만들기 : 프로젝트 안의 기능들 만들기. 기능 단위. 네이버로 따지면 블로그 앱 카페 앱 등 앱 단위
8. model 설계 : 데이터베이스
  <하기 순서가 계속 반복하면서 화면 생성>
  9. view 만들기 : 기능, 계산(어떤어떤 기능을 처리하겠다.)
  10. template 만들기 : 뷰의 결과, 화면에 표시될 내용 및 양식
  11. URL 만들기 : 어떤 주소로 접속해야 이 뷰를 동작하게 할 것인지

CRUD : Create, Read, Update, Delete
 Create : POST
 Read : GET
 Update : PUT/PATCH
 Delete : DELETE
"""
'''
remote displacement : rp와 각 node들이 연결된 선이 rp 기준으로 모인다. 우리가 displacement하는 것은 단지 그 rp 하나 뿐.
rigid 조건 : 거기에 따라 연결된 선이 rigid하면 rigid한 채 따라오는거고
deformable 조건 : rp에서 각 node까지의 연결선 길이가 다르니, 그 선 길이에 따라 받는 하중도 다르게 부과.
	           연결 선이 더 많음 : rp에서의 관계 뿐 아니라 면들과의 관계도 추가적인 수식이 생겨서 관계를 정의.
  	           그리고 그 rp와의 관계를 이용해서 푼다.
'''

from django.contrib import admin
from django.urls import path, include

from myblog.views import index

urlpatterns = [
    path('', index),
    path('bookmark/', include('bookmark.urls')
         ),  # 여기가 1차 병원이라면 bookmark.urls는 2차 병원인 개념. 2차 병원으로 가라고 짬 때리는 코드
    path('admin/', admin.site.urls),  # 관리자 페이지
]
