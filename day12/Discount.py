prices= [100,200,300,400]
print("before discount",prices)
dis=[p*0.9 if p>20 else p for p in prices]
print("after discount",dis)
