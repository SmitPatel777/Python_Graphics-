import turtle as r
import colorsys as sp
r.tracer(2)
r.bgcolor('black')
r.pensize(2)
n=10
h=0
for i in range(50):
    for i in range(4):
        c=sp.hsv_to_rgb(h,1,1)
        h+=1/n
        r.color(c)
        r.circle(50+i*5,90)
        r.forward(50)
        r.left(90)
        r.right(10)
r.done()



#star
# import turtle as r
# import colorsys as sp

# r.speed(0)  
# r.bgcolor('black')
# r.pensize(2)

# n = 100  
# h = 0    

# r.penup()   
# r.goto(0, 200)  
# r.pendown()  

# for i in range(50):  
#     c = sp.hsv_to_rgb(h, 1, 1)  
#     r.color(c)
#     h += 1/n  \
#     for  i in range(5):
#         r.forward(300)  
#         r.right(144)  
#     r.right(36)  

# r.done()  