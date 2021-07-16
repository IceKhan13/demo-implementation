import math 
from typing import Union


class Impl:
    def run(self, x: Union[int, float]) -> Union[int, float]:
        return math.pow(x, 2)
