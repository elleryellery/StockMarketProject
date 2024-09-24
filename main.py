import SQLHandler as sql
import StockHandler as stock

if(sql.update() == 1):
    stock.Trade(sql.latest().?, sql)