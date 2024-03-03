
import threading
import time
import queue

class Btf():

    def __init__(self, tasks, processor_cnt=5):
        pass

    def start(self):
        thread = BtfThread()
        thread.run()
        pass

class BtfProcessor():

    def run(self):
        pass

class BtfThread(threading.Thread):
    
    def run(self):
        while True:
            time.sleep(1)
            print('run')

class BtfQueue():

    def __init__(self, queue):
        self.queue = queue
        self.result_queue = queue.Queue()
        pass

    def get(self):
        pass
        return self.queue.get()

    def put(self, item):
        pass
        return self.queue.put(item)

class Reducer():

    def start(self, queue):
        self.queue = queue
        pass

class ProgressBar():

    def start(self):
        pass

print('dd -> %s' % (1))

items = []

btf = Btf()
btf.start()

