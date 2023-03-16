import tkinter as tk

window = tk.Tk()
window.title('Scale')
window.geometry('200x200')

#做一个列表
l = tk.Label(window,bg='red',width=30,text='empty')
l.pack()

def print_selection(v):
    l.config(text='you have selected'+v)


'''

    设置尺度

    在window中   显示文字

    from_从...开始(from被用过了所以加_)  to到..结束

    设置方向  横向

    showvalue=显示与否  0就是不显示选的  1就是显示选的具体数字

    标签单位长度tickineval  隔几个一显示
 
    保留位数 resolution  1整数  0.1保留一位小数

    命令  command

   
'''

s = tk.Scale(window,label='try me',from_=5,to=11,orient=tk.HORIZONTAL,length=200,showvalue=1,
             tickinterval=3,resolution=0.01,command=print_selection)
s.pack()

window.mainloop()
