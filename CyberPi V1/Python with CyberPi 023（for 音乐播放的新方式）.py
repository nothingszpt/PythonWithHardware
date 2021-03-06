""""
名称：023 For循环 音乐播放的新方式
硬件：童芯派
功能介绍：通过while循环的条件控制循环的结束。

难度：⭐⭐⭐

支持的模式：在线 上传

使用功能解读：
1. 列表 list
   列表可以对不同的数据类型进行存储。列表中的数据用[]围起来，列表内的数据用逗号进行区隔。
   创建空列表：     列表名称 = []
   列表中的元素每一个都用对应的序号，列表中的元素顺序从0开始。
   list[1]  则表示列表list的第二个元素。

2.for循环
  for循环，也被称为有限循环，常用于数据的遍历。
  举例：
      for i in muiscList:
      表示的是用变量i遍历musicList列表中的元素（数据），列表有多长，它就会循环几次。
      用变量i来临时存放每次循环获取的列表元素。

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------

import cyberpi

musicList = [60, 60, 67, 67, 69, 69, 67, 65, 65, 64, 64,
             62, 62, 60, 67, 67, 65, 65, 64, 64, 62]       # 创建列表musicList存放音乐的音调数值
for i in musicList:                                        # for循环遍历列表musicList:
    cyberpi.audio.play_music(i, 0.25, 'piano')                 # 将变量i获取到的数值放在音效播放API对应的参数中。


# 拓展
# 尝试结合For循环，让灯光按照列表中的数值顺序亮起来。注意结合熄灭功能一起使用。

