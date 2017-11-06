#myfunction file


def polygon(t,s,d):#accepts a turtle,sides,distance
    a = 360/s
    for times in range(s):
        t.forward(d)
        t.right(a)

def polygonfill(t,s,d,c):#accepts a turtle,sides,distance
    a = 360/s
    t.color(c)
    t.begin_fill()#fill in the polygon
    for times in range(s):
        t.forward(d)
        t.right(a)
    t.end_fill()

def jump(t,x,y):#parameters
    t.penup()
    t.goto(x,y)
    t.pendown()
    
def cool(t,d,c1,c2):
    t.color(c1)
    polygon(t,4,d)#call to the function polygon
    t.color(c2)
    polygon(t,3,d)

def ballons(t,r):
    for c in ['light blue','blue','light blue','blue']:
        t.begin_fill()
        t.color(c)
        t.circle(r)
        t.right(90)
        t.end_fill()

def stars(t,c):
    for times in range(11):
        star(t,times *10 + 8,c)
        t.penup()
        t.right(30)
        t.forward(50)
        t.pendown()

def fish(t,s,d,c):
    a = 360/s
    t.begin_fill()
    for times in range(s):
        t.color(c)
        t.left(a)
        t.forward(d)
    t.end_fill()

    


        
        
        
        

    




    
