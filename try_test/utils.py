import random
import string


def code_generator2(size=6, chars=string.ascii_lowercase + string.digits):
    '''
    new_code =""
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    '''
    return "".join(random.choice(chars) for _ in range(size))
    #위의 네줄과 사 실상 동일한 코드 임.
    # _ 는 키를 사용하지 않을 경우 쓰이는 placeholder
    # 함수의 선언 부분을 볼것.



def code_generator(size=6, chars="abcdefghijklmnopqrstuvwxyz1234567890"):
    '''
    new_code =""
    for _ in range(size):
        new_code += random.choice(chars)
    return new_code
    '''

    return "".join(random.choice(chars) for _ in range(size))
    #위의 네줄과 사실상 동일한 코드 임.
    # _ 는 키를 사용하지 않을 경우 쓰이는 placeholder



def create_shortcode(instance,size=6):
    new_code = code_generator(size=size)
    print(instance)
    print(instance.__class__)
    print(instance.__class__.__name__)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=new_code).exists()
    if qs_exists :
        print(create_shortcode(size=size))
        return  create_shortcode(size=size)
    return new_code

    # 이렇게 클래스를 인스턴스로 받을수 있다는 것을 잘 볼것
    # 이렇게 하는 이유는 이 메서드 내에서 모델 객체를 가져와야되는데 임포트를 하게되면
    # 상호 참조가 되서 오류가 발생하기 때문.
