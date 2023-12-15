# import colorgram

# using cologram module to extract the colours from an image
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 20)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [(250, 245, 232), (252, 244, 249), (174, 65, 35), (23, 29, 60), (241, 233, 79),
     (51, 35, 21), (143, 23, 36), (207, 147, 98), (53, 28, 36), (118, 164, 212), (144, 25, 18), (56, 84, 137),
     (197, 77, 122), (28, 44, 120), (148, 63, 77), (28, 47, 35), (63, 105, 68), (91, 103, 195)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 ==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)



screen = turtle_module.Screen()
screen.exitonclick()
