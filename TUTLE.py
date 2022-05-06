import turtle
import random # import random module
t = turtle.Turtle()
t.left(90)
t.speed(-5)
t.color('green')
t.pensize(5)
t.screen.title("My Fractal Tree")


def draw_fractal(blen):
     
    # add these two lines
    sfcolor = ["red", "blue", "purple", "grey", "magenta"]
    t.color(random.choice(sfcolor))

    if(blen<10):
        return
    else:

        t.forward(blen)
        t.left(30)
        draw_fractal(3*blen/4)
        t.right(60)
        draw_fractal(3*blen/4)
        t.left(30)
        t.backward(blen)





value = int(input("write value : "))
draw_fractal(value)
