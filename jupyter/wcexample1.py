import wizcoin

purse = wizcoin.WixCoin(2, 5, 99)  # 引数の整数は__init__()に渡される
print(purse)
print('G: ', purse.galleons, 'S: ', purse.sickles, 'K: ', purse.knuts)
print('Total value: ', purse.value())
print('Weight: ', purse.weightInGrams(), 'grams')
print()

coinJar = wizcoin.WixCoin(13, 0, 0)
print(coinJar)
print('G: ', coinJar.galleons, 'S: ', coinJar.sickles, 'K: ', coinJar.knuts)
print('Total value: ', coinJar.value())
print('Weight: ', coinJar.weightInGrams(), 'grams')
