import sys

PRICE_UNIT = 100

class texts:
    title = "#### 클래스 %s 자판기 입니다. ####"
    product = "%s:%s(%s원)"
    insert_coin = "동전을 넣어 주세요. : "
    n_enough_coin = "동전이 부족합니다.\n거스름돈은 %s원 입니다."
    select_product = "원하시는 상품번호를 선택하세요."
    select_fault = "잘 못 누르셨습니다."
    product_out = "선택하신 %s 입니다. 거스름돈은 %s원 입니다."

class Product:
    productType = {"1":"바닐라", "2":"초코", "3":"딸기"}
    productValue = {"1":500, "2":600, "3":700}

class IcecreamVM(Product):
    _name = "아이스크림"

    def __init__(self):
        print(texts.title %self._name)

    def run(self):
        while True:
            try:
                inputCoin = float(input(texts.insert_coin))
            except ValueError: 
                print(texts.select_fault)
            else:
                self.selectProduct(inputCoin)

    def selectProduct(self, coin):
        description = ''
        for selection, item in Product.productType.items():
            price = self.getProductValue(selection)
            description += selection+':'+item+'('+str(price)+'원) '

        print(description)
        inputProduct = input(texts.select_product)
        productValue = self.getProductValue(inputProduct)

        if productValue:
            productName = self.getProductName(inputProduct)
            self.payment(coin, productName, productValue)

        else:
            print(texts.select_fault)
            self.selectProduct(coin)

    def getProductValue(self, product):
        returnValue = 0
        for selection, value in Product.productValue.items():
            if selection == product :
                returnValue = value
        return returnValue

    def getProductName(self, product):
        for selection, name in Product.productType.items():
            if selection == product :
                return name

    def payment(self, coin, name, value):
        coinValue = coin * PRICE_UNIT
        if coinValue >= value:
            balance = coinValue - value
            print(texts.product_out %(name, int(balance)))
        else:
            print(texts.n_enough_coin %int(coinValue))
        self.run()
            
class ChocolateVM(IcecreamVM):
    _name = "초콜릿"

    def __init__(self):
        Product.productType = {"1":"밀크초코", "2":"다크초코", "3":"화이트초코", "4":"스트로베리초코"}
        Product.productValue = {"1":500, "2":600, "3":700, "4":800}


if __name__ == "__main__":
    print("1. 아이스크림, 2:초콜릿")
    select_vm = input("구동할 자판기를 선택하세요.").strip()

    if select_vm == "1":
        vm = IcecreamVM()

    elif select_vm == "2":
        vm = ChocolateVM()

    else:
        print("잘 못 누르셨습니다. 다시 실행 해 주세요.")
        sys.exit(-1)

    try:
        vm.run()

    except KeyboardInterrupt as exc:
        print("판매를 종료합니다.")
