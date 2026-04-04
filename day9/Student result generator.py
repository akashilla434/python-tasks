class result:
    def calculated(self,m1,m2,m3=None):
            if m3 is None:
              total = m1+m2
              print("total(2 subjects):", total)
            else:
              total=m1+m2+m3
              print("total(3 subject):",total)
r = result()
r.calculated(77,87)
r.calculate(70,55,79)
