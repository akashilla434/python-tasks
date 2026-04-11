prices=[100,200,300,400]
dis=[p*0.9 if p>200 else p for p in prices]
new_prices=("after discount",prices)
print(new_prices)
