from Strategy.Stock_bucket import print_result
from Thread_tools.Controller import Controller

if __name__=="__main__":
    #设置线程数
    task=Controller(10)
    task.start()
    task.join()

    #打印下结果
    print_result()
    print("结束")






