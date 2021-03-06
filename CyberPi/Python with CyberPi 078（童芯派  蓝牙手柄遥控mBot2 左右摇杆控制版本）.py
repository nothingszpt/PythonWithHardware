""""
名称：078 童芯派 蓝牙手柄遥控mBot2
硬件： 童芯派
功能介绍：
实现左右摇杆对mBot2小车的控制
程序当中使用了两个四路巡线传感器。

使用到的API及功能解读：
1.import gamepad
导入蓝牙遥控手柄的相关的功能
2.gamepad.get_joystick('摇杆方向')
蓝牙手柄两个摇杆控制的API，括号内填入参数 'Lx' 'Ly' 'Rx' 'Ry'
每个摇杆数值区间如下所示：

          255
-255   摇杆中间为0   255
          -255

3.gamepad.is_key_pressed()
该API用于手柄上的按键是否按下了。

4.math.fabs()
计算绝对值

难度：⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import gamepad
import math
import mbot2


def left_right(x, y):
    mbot2.drive_speed(((gamepad.get_joystick(x) + gamepad.get_joystick(y))) / 2.55, ((gamepad.get_joystick(x) - gamepad.get_joystick(y))) / 2.55)

while True:
    if not (math.fabs(gamepad.get_joystick("Lx"))<3 and math.fabs(gamepad.get_joystick("Ly"))<3):
        left_right('Lx', 'Ly')
    else:
        if not (math.fabs(gamepad.get_joystick("Rx"))<3 and math.fabs(gamepad.get_joystick("Ry"))<3):
            left_right('Rx', 'Ry')
        else:  
            if gamepad.is_key_pressed('Up'):
                mbot2.forward(100)
                cyberpi.led.show('blue blue blue blue blue')
            else:
                if gamepad.is_key_pressed('Down'):
                    mbot2.backward(100)
                    cyberpi.led.show('red red red red red')
                else:
                    if gamepad.is_key_pressed('Left'):
                        mbot2.turn_left(100)
                        cyberpi.led.show('yellow yellow black black black')
                    else:
                        if gamepad.is_key_pressed('Right'):
                            mbot2.turn_right(100)
                            cyberpi.led.show('black black black yellow yellow')
                        else:
                            mbot2.EM_stop("ALL")