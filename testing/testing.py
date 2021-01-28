from multiprocessing import Process
import time


def something(str):
    print(str)
    i=0
    while True:
        i +=1
        print(i)
        time.sleep(1)


if __name__ == "__main__":
    action_process = Process(target=something,name='Something Process',args=('Hello',))

    action_process.start()
    action_process.join(timeout=5)
    action_process.terminate()
    print("Bitch")