# The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"
#
#  LB - Left Bottom point
#  LT - Left Top point
#  RT - Right Top point
#  RB - Right Bottom point
# numbers after letters are the coordinates of a point.
# Write a function figure_perimetr() that calculates the perimeter of a quadrilateral


def figure_perimetr(coord):
    import re
    from math import sqrt

    lb = str(re.findall(r"LB...", coord))
    lt = str(re.findall(r"LT...", coord))
    rt = str(re.findall(r"RT...", coord))
    rb = str(re.findall(r"RB...", coord))
    side1 = sqrt((int(lb[4])-int(lt[4]))**2 + (int(lb[6])-int(lt[6]))**2)
    side2 = sqrt((int(lb[4])-int(rb[4]))**2 + (int(lb[6])-int(rb[6]))**2)
    side3 = sqrt((int(rb[4])-int(rt[4]))**2 + (int(rb[6])-int(rt[6]))**2)
    side4 = sqrt((int(lt[4])-int(rt[4]))**2 + (int(lt[6])-int(rt[6]))**2)
    p = side1+side2+side3+side4
    return(p)

test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))

test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))