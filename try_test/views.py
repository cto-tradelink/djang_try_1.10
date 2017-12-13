from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import *
from django.shortcuts import render, get_object_or_404


# Create your views here.
def shorturl_redirect_view(request,shortcode, *args, **kargs):

    '''
    try:
        obj = ShortUrl.objects.get(shortcode=shortcode)
    except:
        obj = ShortUrl.objects.all().first()
    이 코드는 좋은 코드가 아니다.
    qs = ShortUrl.objects.get(shortcode_iexact=shortcode)
    if qs.exist() and qs.count() == 1:
        obj = qs.first()
        obj_url = obj.url
    이코드가 그나마 좋다.
    더 좋은건 get_object_or_404 를 쓰는 것이다.
    '''
    obj = get_object_or_404(ShortUrl,shortcode=shortcode)
    obj_url = obj.url
    #return HttpResponse("hello {sc}".format(sc=obj_url))
    return HttpResponseRedirect(obj.url) # 해당 url 로 바로 이동~

class ShortUrlCBView(View):
    def get(self,request,shortcode, *args, **kwargs):
    #def get(self,request, slug=None, *args, **kwargs):
        print(args)
        print(kwargs)

        obj = get_object_or_404(ShortUrl, shortcode=shortcode)
        return HttpResponse ("hello again")
    def post(self,request,shortcode, *args, **kwargs):
        some_dict = {}
        #some_dict["url"] 이코드는 에러를 발생 시킴
        #some_dict.get("url","http://google.com") 에러를 발생시키지 않음. url 이 없으면 http://google.com 을 리턴
        return "post"