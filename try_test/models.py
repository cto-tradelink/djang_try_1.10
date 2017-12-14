from django.db import models
from .utils import *
# Create your models here.
from django.conf import  settings   # 이렇게 세팅 파일을 임포트함 왜때문에?
from try_django_0.settings import *  # 이렇게 하면 안되나? 차이가 뭐지?
# django 의 from 에서 경로는 프로젝트의 루트( 여기서는 try_django_0 ) 을 기준으로 함.
# 각 파일이 위치한 곳 기준이 아님( 절대 경로 사용시에 )

from .validator import *


SHORTCODE_MAX = getattr( settings , "SHORTCODE_MAX" , 15)
# 이 코드는  SHORTCODE_MAX = settings.SHORT_CODE 와 같음.
# getattr 를 쓰게 되면 확장성이 좋아진다고 함.
# settings 파일에서 int  를 바꾸게 되면 makemigration + migrate 를 해야함.

class ShortUrlManager(models.Manager):
    def all(self,*args, **kwargs):
        qs_main = super(ShortUrlManager, self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcodes(self, items=None):
        qs = ShortUrl.objects.filter(id__gte=1)
        print(items)
        if items is not None and isinstance(items,int):
            qs = qs.order_by("-id")[:items]
        newcode =0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            newcode += 1
        return "New codes made : {i}".format(i=newcode)

class ShortUrl(models.Model):
    url = models.CharField(max_length=220, validators= [validate_dot_com, validate_url]) # 이렇게 작성해주면 어드민에도 밸리데이터가 적용됨.
    shortcode = models.CharField(max_length=30, unique=True, blank=True)
    #shortcode = models.CharField(max_length=30, null=true) => empty in database is okay
    #shortcode = models.CharField(max_length=30, default="cfe") => 디폴트 옵션
    # null vs blank : https://wayhome25.github.io/django/2017/09/23/django-blank-null/
    # null 은 주어진 데이터베이스 컬럼이 null 값을 가질것인지 아닌지
    # blank 는 폼 유효성 검사를 할지 말지 - 유효성과 관련되어 있다.
    # django 모델 정리 : http://nukggul.tistory.com/17

    updated  = models.DateTimeField(auto_now=True)      # everytime the models is saved.
    timestamp = models.DateTimeField(auto_now_add=True)  # when models was created
    active = models.BooleanField(default=True)

    objects = ShortUrlManager()
    #objects 를 오버라이드 하였음!!!!!

    #class Meta:
    #    ordering = '-id'

    def __str__(self):
        return  self.url
    def save(self, *args, **kargs):
        print("something")
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(ShortUrl, self).save(*args,**kargs)
    def my_save(self):
        #super(ShortUrl, self).save(*args, **kargs) 이걸 쓰면 안됨
        self.save()

    '''
    마이그레이션에서 에러가 생기는 경우
    python manage.py migrate  --fake
    실제 db 구조와 models.py 의 내용이 다른 경
    -------------
    in python shell
    obj3, created = ShortUrl.objects.get_or_create(~~~~~)
    get_or_create : 리턴값은 튜플( 객체, true,false )
    참고 : update_or_create
    print(created)  생성된 object  : 출력은 True Flase
    obj3 = ShortUrl.objects.get_or_create(~~~~~) 로 해도 동일
    print(obj3)  이미 있는 경우 저장된 object

    '''
    def get_absolute_url(self):
        return "htst/{shortcode}".format(shortcode=self.shortcode)