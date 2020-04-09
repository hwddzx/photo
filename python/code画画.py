import random
import time
import turtle


def Tree(branch, t):
    time.sleep(0.0005)
    if branch > 3:
        if 6 <= branch <= 12:  #
            if random.randint(0, 2) == 0:  # 随机绘制
                t.color('snow')  # 设置颜色
            else:
                t.color('lightcoral')  # 树叶颜色
            t.pensize(branch / 3)
        elif branch < 6:
            if random.randint(0, 1) == 0:
                t.color('snow')
            else:
                t.color('lightcoral')  #
            t.pensize(branch / 2)
        else:
            t.color('sienna')  # 赭(zhě)色
            t.pensize(branch / 10)  # 6
        t.forward(branch)
        a = 1.5 * random.random()
        t.right(20 * a)
        b = 1.5 * random.random()
        Tree(branch - 10 * b, t)
        t.left(40 * a)
        Tree(branch - 10 * b, t)
        t.right(20 * a)
        t.up()
        t.backward(branch)
        t.down()


if __name__ == '__main__':
    Tree(50, turtle)
