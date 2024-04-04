'''
ncmlistdownloader/common/thread_test.py
Core.Ver.1.0.0.240402a2
Author: CooooldWind_
Copied from: https://python-parallel-programmning-cookbook.readthedocs.io/zh-cn/latest/chapter2/13_Evaluating_the_performance_of_multithread_applications.html
'''
from threading import Thread

class threads_object(Thread):
    def run(self):
        function_to_run()

class nothreads_object(object):
    def run(self):
        function_to_run()

def non_threaded(num_iter):
    funcs: list[Thread] = []
    for i in range(int(num_iter)):
        funcs.append(nothreads_object())
    for i in funcs:
        i.run()

def threaded(num_threads):
    funcs: list[Thread] = []
    for i in range(int(num_threads)):
        funcs.append(threads_object())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()

def function_to_run():
    pass

def show_results(func_name, results):
    print("%-23s %4.6f seconds" % (func_name, results))

def best_thread_single():
    from timeit import Timer
    repeat = 50
    number = 1
    num_threads = [1, 2, 4, 8, 16, 32, 64]
    for i in num_threads:
        t = Timer("non_threaded(%s)" % i, "from __main__ import non_threaded")
        result_a = sum(t.repeat(repeat = repeat, number = number)) / repeat
        t = Timer("threaded(%s)" % i, "from __main__ import threaded")
        result_b = sum(t.repeat(repeat = repeat, number = number)) / repeat
        if result_a  * 500 < result_b:
            return i // 2

def best_thread(time = 10):  
    k = 0
    for i in range(time):
        j = best_thread_single()
        print(j)
        k += j
    num_threads = [1, 2, 4, 8, 16, 32, 64]
    k /= time
    for i in num_threads:
        if i > k:
            return i // 2