from collections import deque
from statistics import median
from typing import Iterable, Iterator, TypeVar, Deque, Optional

T = TypeVar("T", int, float)

def chunks(iterable: Iterable[T], size: int) -> Iterator[list[T]]:
    '''chunk the iterable'''
    buffer = [] #this empty list will act as the buffer
    for item in iterable:
        buffer.append(item)
        buf_size = len(buffer)
        if len(buffer)== size: #when the chunk reached its size
            yield buffer #yield the chunk(this will halt the loop)
            buffer = [] #reset the buffer
    if buffer: # to atch the leftovers
        yield buffer 

def moving_average(window: int):
    '''Calculate the moving avarage'''
    buffer = deque(maxlen=window) #double_ended_queue of given size to calculate the moving avg
    avg = None #initial avarage
    while True:
        x = yield avg #load x(overwrite the variable)
        buffer.append(x) # load into the double ended queue
        avg = sum(buffer)/len(buffer) #calculate the avarage


def moving_median(window: int):
    '''Finding the moving median'''
    buffer = deque(maxlen=window) #similar implementation as the moving avarage
    med = None  #initialize the median
    while True:
        x = yield med #load values
        buffer.append(x) #load into the deque
        med = median(buffer) #calculate the median(moving median)