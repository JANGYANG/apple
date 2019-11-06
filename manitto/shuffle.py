from collections import deque
import random

def shuffle():
    
    from manitto.models import Apple
    Apple.objects.all().delete()
    Apple(name="이우경",phone="+8201095233114").save()
    Apple(name="곽태연",phone="+8201068901992").save()
    Apple(name="강원영",phone="+8201045202092").save()
    Apple(name="권혁승",phone="+8201079176167").save()
    Apple(name="나길수",phone="+8201021155566").save()
    Apple(name="김민국",phone="+8201041946865").save()
    Apple(name="배정윤",phone="+8201033874168").save()
    Apple(name="이세령",phone="+8201027981809").save()
    Apple(name="이유정",phone="+8201065388521").save()
    Apple(name="장지웅",phone="+8201072456513").save()
    Apple(name="장지혁",phone="+8201066037085").save()
    Apple(name="제갈솔아",phone="+8201050125729").save()
    Apple(name="조경진",phone="+8201048041663").save()
    Apple(name="최은진",phone="+8201049494673").save()
    Apple(name="최태림",phone="+8201020594306").save()

    apple = Apple.objects.all()

    firstNum = apple.first().appleId
    lastNum = apple.last().appleId
    deq = deque(random.sample(range(firstNum, lastNum+1), len(apple)))
    
    
    while apple.get(appleId = deq[0]).manittoId is None:
        a = apple.get(appleId = deq[0])
        deq.rotate()
        a.manittoId = apple.get(appleId = deq[0])
        a.save()

