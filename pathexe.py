import os

exe_file_name = input("Please input file name of the exe: ")

env_dist = os.environ  # environ是在os.py中定义的一个dict environ = {}
# print(env_dist['PATH'])  # 或 print(env_dist.get('PATH'))
pa = env_dist['PATH']
palst = ['.']
palst.extend(pa.split(';'))
print('\nThe first path for the exe:')
for p in palst:
    exep = p + '\\' + exe_file_name      # '\\conda.exe'              # '\\pyinstaller.EXE'
    if os.path.exists(exep):
        print('【', exep, '】')
        break
else:
    print('【Nothing】')

# 打印所有环境变量，遍历字典 (不只是PATH)
# for key in env_dist:
#     print(key + ' : ' + env_dist[key])
