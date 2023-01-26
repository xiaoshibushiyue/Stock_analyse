from Thread_tools.Controller import Controller

if __name__=="__main__":
    #设置线程数
    task=Controller(10)
    task.start()
    task.join()
    print("结束")






