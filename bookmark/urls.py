from django.urls import path, include
from .views import BookmarkCreateView, BookmarkDeleteView, BookmarkDetailView, BookmarkListView, BookmarkUpdateView

urlpatterns = [
    # path('어떤 주소로 접속하겠다', '어떤 view를 동작시키겠다')
    # as_view() : 클래스형 뷰를 함수형 뷰로 바꿔주는 효과, 괄호 꼭 넣어야 한다.
    path('', BookmarkListView.as_view(), name='list'),
    path("add/", BookmarkCreateView.as_view(), name="add"),
    path("detail/<int:pk>/", BookmarkDetailView.as_view(), name="detail"
         ),  # <int:pk> : detail 뒤에 해당 글번호 입력, 웹사이트에서 자주 봤음, primary key
    path("update/<int:pk>/", BookmarkUpdateView.as_view(), name="update"),
    path("delete/<int:pk>/", BookmarkDeleteView.as_view(), name="delete"),
]
