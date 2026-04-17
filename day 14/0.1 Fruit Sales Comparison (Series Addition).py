import pandas as pd
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
print("Given Series are\n",S1,'\n',S2)
total=S1+S2
print("Individual Sales are:\n",total)
s1=sum(S1)
s2=sum(S2)
aft=s1+s2
print("Total sales of all fruits is:",aft)
