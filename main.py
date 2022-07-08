# from typing import List, Tuple, Any
#
# import colorgram
# extract colors from image:
# colors = colorgram.extract('Снимок экрана 2022-07-08 в 11.48.55 PM.jpg', 16)
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
# print(rgb_colors)
import turtle as turtle_module
import random
# set format of colors rgb:
turtle_module.colormode(255)

timmy = turtle_module.Turtle()
timmy.speed("fast")
color_list = [(229, 207, 217), (248, 215, 245), (217, 176, 189), (182, 143, 160), (168, 102, 134), (253, 102, 254),
(222, 11, 211), (138, 86, 111), (213, 178, 178), (197, 176, 176)]
timmy.penup()
# Make the turtle invisible:
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100
for dot_count in range(1, number_of_dots + 1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)
    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
