import turtle as t


def spiral(len):
    if len <= 5:
        return
    t.forward(len)
    t.right(90)
    spiral(len-5)


t.speed(0)
spiral(1000)
t.hideturtle()
t.done()
