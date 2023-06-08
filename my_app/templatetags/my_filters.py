from django import template
import math

register = template.Library()

@register.filter
def divide_by(value, arg):
    return value / arg

@register.filter
def greaterThan(value, arg):
    return value > arg



@register.filter
def rgbReturn(value):
    #Function for changing the colour of the bar for the student's grades.
    if (value < 50):
        return "rgb(255, 255, 0)"
    elif (value >= 50 and value < 70):
        return "rgb(204, 255, 51)"
    elif (value >= 70 and value < 80):
        return "rgb(153, 255, 51)"
    elif (value >= 80):
        return "rgb(102, 255, 51)"