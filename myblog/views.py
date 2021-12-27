'''
뷰 : 기능을 담당(페이지 단위)
화면이 나타나는 뷰, 화면이 없는 뷰
화면이 있건 없건 주소 url은 있어야 한다.

뷰 내용(함수, 클래스), url이 있으면 동작한다.

뷰의 코드 형식 : 함수형 or 클래스형
 - 함수형 : request를 매개변수로 받고(추가 매개변수 가능), 모양은 함수
            내가 원하는대로 동작들을 설계하고 만들고 싶을 때
- 클래스형 : CRUD, 기존에 많이 사용하는 기능을 미리 클래스로 만들어두고
            상속하여 받아 사용한다.

장고는 장고의 제네릭 뷰를 많이 사용함
'''
from django.http import HttpResponse


# 함수형 view
def index(request):  # request : 사용자가 웹브라우저를 통해 요청한 정보 포함
    return HttpResponse("This is First Page.")
