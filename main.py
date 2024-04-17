#import colorgram
import turtle as t
import random

# colors = colorgram.extract('image.jpg', 30)
# colors_rgb = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     colors_rgb.append(new_color)
# print(colors_rgb)
t.speed("fastest")
color_list = [(237, 252, 245), (249, 228, 18), (212, 13, 9), (197, 12, 35), (197, 69, 20), (32, 90, 188), (43, 212, 70), (234, 149, 40), (33, 31, 152), (16, 22, 55), (66, 9, 48), (240, 245, 251), (244, 39, 149), (65, 203, 229), (14, 205, 222), (63, 21, 10), (223, 20, 110), (229, 164, 9), (15, 154, 23), (245, 57, 16), (98, 75, 9), (248, 11, 9), (223, 139, 203), (67, 241, 160), (10, 97, 61), (5, 38, 33), (67, 219, 155)]
t.penup()
t.hideturtle()

t.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)
num_of_dots = 101

for dot_count in range(1, num_of_dots):
    t.dot(10, random.choice(color_list))
    t.forward(50)
    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)


screen = t.Screen()
screen.exitonclick()






