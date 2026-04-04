class circle:
    def area(self):
        r = 3
        print("circle area:",3.18 *r*r)
class rectangle:
    def area(self):
        l=4
        w=8
        print("rectangle area:",1*w)
class triangle:
    def area(self):
        b=6
        h=2
        print("triangle area:",0.5*b*h)
shapes=[circle(),rectangle(),triangle()]
for s in shapes:
    s.area()
