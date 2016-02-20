#-*-coding: utf-8 -*-

import time
from delay import Delayer

__author__ = 'pb'

if __name__ == "__main__":

    @Delayer.delay(4)
    def test(key):
        print("The thread: {key} run at {time}".format(key=key, time=str(time.time())))

    print("Now:" + str(time.time()))
    test("First")  # will run after 4 seconds

    time.sleep(5)
    print("Now:" + str(time.time()))
    test("Second")  # Won't run
    time.sleep(2)
    test("Third")   # will run after 6 seconds

