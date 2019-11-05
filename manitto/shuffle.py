from collections import deque
import random

def shuffle(apple):
    firstNum = apple.first().appleId
    lastNum = apple.last().appleId
    deq = deque(random.sample(range(firstNum, lastNum+1), len(apple)))
    
    
    while apple.get(appleId = deq[0]).manittoId is None:
        a = apple.get(appleId = deq[0])
        deq.rotate()
        a.manittoId = apple.get(appleId = deq[0])
        a.save()

