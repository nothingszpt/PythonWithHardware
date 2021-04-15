""""
名称：EXT 006 童芯派 视觉模块 飞机大战 视觉控制
硬件： 童芯派 
功能介绍：
将视觉模块识别的目标，作为控制角色飞机的方式。即视觉模块识别到目标所在的区域映射至童芯派的屏幕
位置上。



难度：⭐⭐⭐⭐⭐
支持的模式：上传模式
无

"""
# ---------程序分割线----------------程序分割线----------------程序分割线----------
import cyberpi
import time
import random
import math
import mbuild


class Plane:
    def __init__(self):
        self.plane = cyberpi.sprite()
        self.plane.draw_pixels(
            [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff,
             0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x1eaaff, 0x1eaaff,
             0x1eaaff, 0x1eaaff, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000])
        self.x = 64
        self.y = 64
        self.plane.set_align('center')
        self.plane.move_to(self.x, self.y)
        self.point = 0

    def move_detect(self):
        self.x = 128-(mbuild.smart_camera.get_sign_x(1, 1) / 2.5)
        self.y = mbuild.smart_camera.get_sign_y(1, 1) / 1.875
        if self.x < 0:
            self.x = 5
        if self.x > 128:
            self.x = 123
        if self.y < 0:
            self.y = 5
        if self.y > 128:
            self.y = 123
        if self.x and self.y <= 0:
            self.point += 1
        self.plane.move_to(self.x, self.y)

    def collide(self, item):
        self.move_detect()
        for i in item:
            if self.plane.is_touch(i.enemy):
                cyberpi.audio.play('prompt-tone')
                i.enemy.hide()
                self.point += 1
                num = math.floor(self.point / 4)
                cyberpi.led.off(id=6-num)
                cyberpi.led.on('r', id= 6-num)
            if self.point == 20:
                return -1


class Enemy:
    def __init__(self):
        self.x = random.randint(0, 128)
        self.y = -1
        self.enemy = cyberpi.sprite()
        self.enemy.draw_pixels(
            [0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623,
             0xf5a623, 0xf5a623, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0xf5a623, 0xf5a623, 0xf5a623, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000,
             0x000000, 0x000000, 0x000000, 0x000000, 0x000000, 0x000000])
        self.enemy.set_align("center")
        self.enemy.set_brush(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.enemy.move_to(self.x, self.y)
        self.speed = random.randint(2, 6)

    def speed_up(self):
        self.speed += 2
        if self.speed >= 30:
            self.speed = 30


    def start(self):
        self.enemy.set_brush(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.x = random.randint(2, 125)
        self.y = -1
        self.enemy.move_to(self.x, self.y)
        self.enemy.show()

    def move(self):
        if self.enemy.get_y() > 128:
            self.start()
        else:
            self.enemy.move_y(self.speed)



mbuild.smart_camera.set_mode("color", 1)
plane = Plane()
count = 0
enemy_list = []
for i in range(0,5):
    enemy_list.append(Enemy())
cyberpi.led.on('b')
while True:
    if plane.collide(enemy_list) == -1:
        cyberpi.display.label("游戏结束",24, 'center')
        time.sleep(2)
        cyberpi.display.label("得分："+ str(count), 24, 'center')
        break
    for j in enemy_list:
        j.move()
    if cyberpi.timer.get() > 10:
        for j in enemy_list:
           j.speed_up()
        cyberpi.timer.reset()
        count += 10
    cyberpi.screen.render()

