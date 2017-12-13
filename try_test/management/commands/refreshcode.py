# 폴더의 구조를 유사하게 하고 각 명령어가 파일이 름이 되게끔 꾸미면 됨... 이거 신기..


from django.core.management.base import BaseCommand, CommandError

from try_test.models import *

class Command(BaseCommand):
    help = "refreshes all url codes"
    def add_arguments(self, parser):
        parser.add_argument("--items", type=int)
        #parser.add_argument("number2", type=int)
        #parser.add_argument("number3", type=int)

    def handle(self,*args,**options):
        print( options)
        return ShortUrl.objects.refresh_shortcodes(items=options['items'])