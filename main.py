import SQLHandler as sql
import StockHandler as stock
import random

index = random.randrange(0,sql.numRows())
print('chosen index: ' + str(index))

row = sql.retrieveRow(index)

print(row)

pl_name = row[0]
discoverymethod = row[1]
pl_dens = row[2]
pl_orbtper = row[3]
pl_massj = row[4]
pl_letter = row[5]

buying = pl_letter == 'b'

quantity = 0
if(len(str(pl_dens))>0):
    quantity = float(pl_dens)*10
elif(len(str(pl_orbtper))>0):
    quantity = float(pl_orbtper)/100000
elif(len(pl_massj)>0):
    quantity = float(pl_massj)*10
else:
    quantity = len(discoverymethod)

quantity = round(quantity)

print('Buying?: ' + str(buying))
print('Starting letter: ' + pl_name[0])
print('Quantity: ' + str(quantity))

if(buying):
    stock.Trade(pl_name[0], quantity)
else:
    stock.Sell()