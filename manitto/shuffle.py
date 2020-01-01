from collections import deque
import random

def shuffle():
    
    from manitto.models import Apple
    
    apple = Apple.objects.all()

    if len(apple) == 0:
        return

    for a in apple:
        a.manittoId = None
        a.save()
    
    firstNum = apple.first().appleId
    lastNum = apple.last().appleId
    deq = deque(random.sample(range(firstNum, lastNum+1), len(apple)))
    
    
    while apple.get(appleId = deq[0]).manittoId is None:
        a = apple.get(appleId = deq[0])
        deq.rotate()
        a.manittoId = apple.get(appleId = deq[0])
        a.save()

