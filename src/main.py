import ccxt.async_support as ccxt
import asyncio

# print(ccxt.exchanges)

# exchange = ccxt.okcoinusd()

# id = 'btcchina'
# btcchina = eval ('ccxt.%s ()' % id)
# print(btcchina)

# binance = getattr(ccxt, 'binance')()
# print(binance)

symbol = 'BUSD/USDT'


async def print_ethbtc_ticker():
    exchange = ccxt.binance({
        'enableRateLimit': True,
    })
    await exchange.load_markets()
    # print(exchange.market (symbol))
    print(await exchange.fetch_ticker(symbol))
    await exchange.close()

asyncio.get_event_loop().run_until_complete(print_ethbtc_ticker())
# print(exchange.symbols)
