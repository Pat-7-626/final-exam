import turtle
import random


class Polygon:
    def __init__(self, num_sides, size, orientation, location, color,
                 border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360 / self.num_sides)
        turtle.penup()


def get_new_color():
    return (random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255))


# draw a polygon at a random location, orientation, color,
# and borderline thickness
def random_polygon(side, time):
    reduction_ratio = 0.618

    num_sides = side  # triangle, square, or pentagon
    size = random.randint(50, 150)
    orientation = random.randint(0, 90)
    location = [random.randint(-300, 300), random.randint(-200, 200)]
    color = get_new_color()
    border_size = random.randint(1, 10)
    polygon = Polygon(num_sides, size, orientation, location, color,
                      border_size)
    polygon.draw_polygon()

    turtle.penup()
    turtle.forward(size * (1 - reduction_ratio) / 2)
    turtle.left(90)
    turtle.forward(size * (1 - reduction_ratio) / 2)
    turtle.right(90)
    location[0] = turtle.pos()[0]
    location[1] = turtle.pos()[1]

    for i in range(time):
        size *= reduction_ratio
        polygon = Polygon(num_sides, size, orientation, location, color,
                          border_size)
        polygon.draw_polygon()



pattern = int(input("Which art do you want to generate? Enter a number between 1 to 8, inclusive: "))

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

if pattern == 1:
    for i in range(20):
        random_polygon(3, 0)
elif pattern == 2:
    for i in range(20):
        random_polygon(4, 0)
elif pattern == 3:
    for i in range(20):
        random_polygon(5, 0)
elif pattern == 4:
    for i in range(7):
        random_polygon(3, 0)
        random_polygon(4, 0)
        random_polygon(5, 0)
elif pattern == 5:
    for i in range(20):
        random_polygon(3, 5)
elif pattern == 6:
    for i in range(20):
        random_polygon(4, 5)
elif pattern == 7:
    for i in range(20):
        random_polygon(5, 5)
elif pattern == 8:
    for i in range(7):
        random_polygon(3, 5)
        random_polygon(4, 5)
        random_polygon(5, 5)

# hold the window; close it by clicking the window close 'x' mark
turtle.done()
