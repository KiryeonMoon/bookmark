from django.db import models
from django.urls import reverse

# Create your models here.
# 데이터베이스에 뭔가를 저장하고 싶으면, 모델을 만들어야 한다.
'''
목적1. 데이터베이스를 sql 없이 다루려고 모델을 사용
목적2. 우리가 데이터를 객체화해서 다루려고 model 사용

모델 = 데이터베이스의 테이블 : 엑셀의 한 시트
모델의 필드(변수들) = 테이블의 컬럼 : 엑셀 시트의 열(A, B, C...)
모델의 인스턴스 = 테이블의 레코드 : 엑셀 시트의 행(1, 2, 3...)
필드의 값 = 변수에 대입되는 값 : 실제 셀에 들어있는 값
'''


# bookmark 모델
class Bookmark(models.Model):  # Bookmark라는 모델 생성(모델을 만들 땐 앞글자는 대문자)
    # 이 모델 안의 필드들(site_name, url 등)이 데이터베이스에 저장될 필드=컬럼값들
    site_name = models.CharField(max_length=100)  # 필드를 추가하되 그 필드의 종류(char) 명시
    url = models.URLField('Site URL')  # 필드를 추가하되 그 필드의 종류(url) 명시
    '''
    필드의 종류가 결정하는 것
    1. 데이터베이스의 컬럼 종류(글자, 숫자 등)
    2. 제약사항(글자 갯수 등)
    3. Form의 종류
    4. Form에서의 제약사항
    '''

    # 클래스의 인스턴스를 출력했을 때 나오는 내용은 str메소드를 사용하면 내용을 바꿀 수 있다.
    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url  # 이런 이름으로 반환해줌

    def get_absolute_url(self):
        return reverse("detail", args=[self.id])


# 모델을 만들었다 = 데이터베이스에 어떤 데이터를 어떤 형태로 넣을 지 결정했다 : 아직 데이터베이스에 넣을 준비가 끝나지 않음
# 마이그레이션(migration)을 하면 데이터베이스에 모델의 내용을 반영 : 테이블, 컬럼 등 생성
# makemigrations = 모델의 변경사항을 추적해서 기록해놓는 정보
# 모델을 수정하고 나면, 마이그레이션을 다시 해 줘야 한다.(중요)