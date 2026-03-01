import turtle

turtle.Screen().bgcolor('blue')

turtle.Screen().setup(500,600)

p = turtle.Turtle()
p.color('white')
p.pensize(1)

n=6

for i in range(n):
    p.forward(167)
    p.right(360/n)

turtle.done()