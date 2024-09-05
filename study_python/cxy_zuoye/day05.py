# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   RONGHUA
# FileName:      day05.py
# Author:       陈啸宇
# Datetime:     2024/8/2 17:45
# Description:
# ---------------------------------------------------------------------------
# 1.定义一个汽车类，在类中定义一个drive方法来描述车辆的信息，然后分别创建BMW 3，Audi A6，Benz C三个对象。每辆汽车具有型号、颜色、马力、价格等属性，其中Benz C还有一个特有的属性：生产日期。
class Car:
    def __init__(self, xinghao, color, mali, price,date=None):
        self.xinghao = xinghao
        self.color = color
        self.mali = mali
        self.price = price
        self.date = date
    def drive(self):
        if self.date == None:
            print(f"这是一辆{self.color}的{self.xinghao}，马力为{self.mali}，价格为{self.price}")
        else:
            print(f"这是一辆{self.color}的{self.xinghao}，马力为{self.mali}，价格为{self.price}，生产日期为{self.date}")



BMW3 = Car("BMW 3", "黑色", 200, 300000)
BMW3.drive()
AudiA6 = Car("Audi A6", "白色", 250, 400000)
AudiA6.drive()
BenzC = Car("Benz C", "红色", 300, 500000,'2024-08-02')
BenzC.drive()

# 2.通过继承实现员工工资计算并打印的功能。
# 父类：员工类
# Ø	属性：姓名、单日工资、工作天数
# Ø	方法：计算打印工资
# 子类：部门经理类和普通员工类。
# Ø	属性：新增一个工资等级
# Ø	方法：重写父类的计算打印工资方法
# 工资计算公式：
# 1.部门经理工资=1000+单日工资*工作天数*工资等级（1.2）
# 2.普通员工工资=单日工资*工作天数*工资等级（1.0）
class yuangong:
    def __init__(self,name,gongzi,zongzuotianshu):
        self.name = name
        self.gongzi = gongzi
        self.zongzuotianshu = zongzuotianshu
    def jisuan(self):
        print(f"{self.name}的工资为{self.gongzi*self.zongzuotianshu}")

class bumenjingli(yuangong):
    def __init__(self,name,gongzi,zongzuotianshu,dengji):
        super().__init__(name,gongzi,zongzuotianshu)
        self.dengji = dengji
    def jinglijisuan(self):
        print(f"{self.name}的工资为{1000+self.gongzi*self.zongzuotianshu*self.dengji}")

class putongyuangong(yuangong):
    def __init__(self,name,gongzi,zongzuotianshu,dengji):
        super().__init__(name,gongzi,zongzuotianshu)
        self.dengji = dengji
    def jinglijisuan(self):
        print(f"{self.name}的工资为{self.gongzi*self.zongzuotianshu*self.dengji}")

d = bumenjingli("陈",1000,30,1.2)
d.jinglijisuan()
c = putongyuangong("张",1000,30,1.0)
c.jinglijisuan()

# 3.实现许三多开枪的需求
# 具体要求：士兵许三多有一把枪，型号是AK47，他可以选择开火。每次开火，子弹数量减少一颗，初始默认子弹3颗。当子弹个数为0时，士兵可以装填子弹，每次只能装填一个。
# 提示：创建一个枪类（属性：型号，方法：发射子弹，装填子弹）和士兵类（属性：姓名，方法：开火），在士兵类中调用枪类的发射子弹和装填子弹方法完成开火以及装弹的操作。
class qiang:
    maxzidan = 3
    def __init__(self, xinghao):
        self.xinghao = xinghao
        self.zidan = self.maxzidan
    def fashe(self):
        if self.zidan > 0:
            self.zidan -= 1
            print(f"当前子弹数量为{self.zidan}")
        else:
            print("子弹已用完")
    def zuangtian(self):
        if self.zidan < self.maxzidan:
            self.zidan += 1
            print(f"当前子弹数量为{self.zidan}")
        else:
            print("子弹已装满")

class shibing(qiang):
    def __init__(self, xinghao,name):
        super().__init__(xinghao)
        self.name = name
    def shoot(self):
        try:
            while 1:
                i = int(input('输入1开火，输入2装弹:'))
                if i == 1:
                    self.fashe()
                elif i == 2:
                    self.zuangtian()
                else:
                    break
        except:
            print("输入错误")

cxy = shibing('AK47',"陈")
cxy.shoot()







