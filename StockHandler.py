import os 
import random
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import GetOrdersRequest
from alpaca.trading.enums import OrderSide, QueryOrderStatus


API_KEY_ID = os.getenv("KEY")
API_SECRET_KEY = os.getenv("SECRET")

trading_client = TradingClient(API_KEY_ID, API_SECRET_KEY, paper=True)

def Trade(letter, _qty):
    assets = trading_client.get_all_assets()
    tradable_stocks = [asset for asset in assets if asset.tradable and asset.asset_class == 'us_equity']
    
    options = []
    
    for stock in tradable_stocks:
        if(stock.symbol[0] == letter):
            options.append(stock.symbol)

    if(len(options) == 0):
        Sell()
    else:
        _symbol = options[random.randrange(0, len(options))]
        
        print('Buying: ' + _symbol)
        
        market_order_data = MarketOrderRequest(
                            symbol=_symbol,
                            qty=_qty,
                            side=OrderSide.BUY,
                            time_in_force=TimeInForce.DAY
                            )

        market_order = trading_client.submit_order(
                        order_data=market_order_data
                    )

def Sell():
    request_params = GetOrdersRequest(
                    status=QueryOrderStatus.ALL,
                    side=OrderSide.BUY
                 )

    orders = trading_client.get_orders(filter=request_params)    
    
    o = orders[random.randrange(0, len(orders))]
    
    oqty = float(o.qty)
    
    if(oqty>1):
        _qty = random.randrange(1,round(oqty))
    else:
        _qty = o.qty
    
    print('Selling: ' + o.symbol + ', quantity' + str(_qty))

    market_order_data = MarketOrderRequest(
                        symbol=o.symbol,
                        qty=_qty,
                        side=OrderSide.SELL,
                        time_in_force=TimeInForce.DAY
                        )

    market_order = trading_client.submit_order(
                    order_data=market_order_data
                )
        