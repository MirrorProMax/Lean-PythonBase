import multiprocessing
import threading

def loop():
    while True:
        pass

if __name__ == "__main__":
    for i in range(multiprocessing.cpu_count()-1):#减1是为了给CPU留一个核心
        print("第",i+1,"个CPU核心")
        t = threading.Thread(target=loop)#用多线程不会轻易占满CPU
        #不管开启多少个线程,同一时间只有一个线程在运行
        #如果需要跑满CPU,则需要使用多进程
        t.start()