# -*- coding:utf-8 -*-
"""
tkinter.filedialog.asksaveasfilename():选择以什么文件名保存，返回文件名
tkinter.filedialog.asksaveasfile():选择以什么文件保存，创建文件并返回文件流对象
tkinter.filedialog.askopenfilename():选择打开什么文件，返回文件名
tkinter.filedialog.askopenfile():选择打开什么文件，返回IO流对象
tkinter.filedialog.askdirectory():选择目录，返回目录名
tkinter.filedialog.askopenfilenames():选择打开多个文件，以元组形式返回多个文件名
tkinter.filedialog.askopenfiles():选择打开多个文件，以列表形式返回多个IO流对象
"""
"""
if __name__ == '__main__':
    try:
        pass
    except Exception as e:
        print(e)
"""
# ### 文件选择对话框#2--返回文件夹：隐藏root窗口, 结果直接打印（不到窗口）：
import tkinter as tk
from tkinter.filedialog import askdirectory
import os


# askdirectory()  # 选择目录
def xz():
    file_path = askdirectory(initialdir='c:/', title='get the path')
    if file_path != '':
        lb.config(text="您选择的文件夹是：" + file_path)
        print( file_path )
        # print('\nThe first path for the exe:')
        for p in os.listdir(file_path):
            filep = os.path.join(file_path, p)
            if os.path.isfile(filep):  # 没路径的文件不能直接用
                print('file: 【', filep, '】')
                # break
        else:
            print('【for循环结束】')
    else:
        lb.config(text="您没有选择任何文件夹")


root = tk.Tk()  # 由于上边 root.withdraw()了，所以需要这行。
btn = tk.Button(root, text="请选择一个文件夹...", command=xz)
btn.pack()
lb = tk.Label(root, text='')
lb.pack()
bquit = tk.Button(root, text='退出', command=root.quit)
bquit.pack()
root.mainloop()

"""  # 注意路径连接符变成了“/”:
C:/
file: 【 C:/$WINRE_BACKUP_PARTITION.MARKER 】
file: 【 C:/DumpStack.log.tmp 】
file: 【 C:/hiberfil.sys 】
file: 【 C:/pagefile.sys 】
file: 【 C:/swapfile.sys 】
file: 【 C:/高考 志愿20200723 没用了.zip 】
【for循环结束】
"""
