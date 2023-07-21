"""
    自定义进程类
"""
import time
from multiprocessing import Process


class MyProcess(Process):
    def __init__(self, value):
        self.value = value
        super().__init__()

    def func1(self):
        time.sleep(3)
        print("步骤1")



    def run(self):
        self.func1()
        self.func2()


if __name__ == '__main__':
    p = MyProcess("3")
    p.start()
    p.join()