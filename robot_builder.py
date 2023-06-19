import turtle as t

def rectangle(horizontal, vertical, color):
    t.pendown()
    t.pensize(1)
    t.color(color)
    t.begin_fill()
    for counter in range(1, 3):
        t.forward(horizontal)
        t.right(90)
        t.forward(vertical)
        t.right(90)
    t.end_fill()
    t.penup()

def draw_smiling_mouth():
    t.goto(-65, 140)
    t.pendown()
    t.pensize(2)
    t.color('black')
    t.setheading(-60)  # Set the initial angle for the smile
    t.circle(25, 120)  # Draw an arc for the smile
    t.penup()

t.penup()
t.speed('slow')
t.bgcolor('Dodger blue')

# Feet
t.goto(-100, -150)
rectangle(50, 20, 'Navy')
t.goto(-30, -150)
rectangle(50, 20, 'Navy')

# Legs
t.goto(-25, -50)
rectangle(15, 100, 'maroon')
t.goto(-55, -50)
rectangle(-15, 100, 'maroon')

# Body
t.goto(-90, 100)
rectangle(100, 150, 'forest green')

# Arms
t.goto(-150, 70)
rectangle(60, 15, 'peru')
t.goto(-150, 110)
rectangle(15, 40, 'peru')

t.goto(10, 70)
rectangle(60, 15, 'peru')
t.goto(55, 110)
rectangle(15, 40, 'peru')

# Neck
t.goto(-50, 120)
rectangle(15, 20, 'grey')

# Head
t.goto(-85, 170)
rectangle(80, 50, 'gold')

# Eyes
t.goto(-60, 160)
rectangle(30, 10, 'white')
t.goto(-55, 155)
rectangle(5, 5, 'black')
t.goto(-40, 155)
rectangle(5, 5, 'black')

# Mouth
draw_smiling_mouth()

t.hideturtle()
t.done()
