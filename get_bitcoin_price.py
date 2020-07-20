import cbpro
import time

public_client = cbpro.PublicClient()
previousPrice = 0


def getBitcoinPrice():
    currentPrice = public_client.get_product_ticker(product_id='BTC-USD').get('price')
    return currentPrice
  
def main(executionInterval):
    global previousPrice
    currentPrice = float(getBitcoinPrice())
    if (currentPrice > previousPrice):
        print("The value of BTC went increased to",currentPrice,"from",previousPrice)
    elif (currentPrice == previousPrice):
        print("The value of BTC has not changed","from",previousPrice)
    else:
        print("The value of BTC has decreased to",currentPrice,"from",previousPrice)
    previousPrice = currentPrice
    time.sleep(executionInterval)
    main(executionInterval)

main(60)