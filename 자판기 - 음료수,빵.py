"""
클래스 실습-자판기 완성하기

"""

import sys

# 가격은 100원 단위이므로 PRICE_UNIT 상수 값을 100으로 선언한다.
# 생략
PRICE_UNIT = 1

class texts:
    title          = "#### 클래스 %s 자판기 입니다. ####"
    product        = "%s:%s(%s원)"
    insert_coin    = "동전을 넣어 주세요. : "
    n_enough_coin  = "동전이 부족합니다.\n거스름돈은 %s원 입니다."
    select_product = "원하시는 상품번호를 선택하세요."
    select_fault   = "잘 못 누르셨습니다."
    product_out    = "선택하신 %s 입니다. 거스름돈은 %s원 입니다.\n감사합니다."

class Product:
    # 제품 종류, 가격을 코드변경없이 데이터를 쉽게 추가하거나 변경할 수 있다.
    productType = {"1":"파워에이드", "2":"2%", "3": "사이다"}
    productValue = {"1":700 , "2":800, "3":900}

           
class BeverageVM(Product):
    _name = "음료수"
 
    def __init__(self):
       # 사용자가 자판기 종류를 선택하면 _name 출력한다.
       print( texts.title %self._name)
 
    def run(self):
        while True:
           try:
               inputCoin = float(input(texts.insert_coin))
           except ValueError:
               # 잘못된 값을 입력받으면 에러 메시지를 출력한다.
               print(texts.select_fault)
           else:
               self.selectProduct(inputCoin)   

    def selectProduct(self, coin):
       # 제품 종류를 리스트로 선언하여 코드변경없이 데이터를 동적으로 보여준다.
       description = ''
       for selection, item  in Product.productType.items():
           # 제품 가격을 가져온다.
           price = self.getProductValue(selection)
           description += selection+':'+item+'('+str(price)+'원) '

       print(description)
       inputProduct = input( texts.select_product )
       productValue = self.getProductValue(inputProduct)

       # 입력한 값에 해당하는 내용이 리스트에 없으면 0이 반환된다.
       if productValue:
          productName = self.getProductName(inputProduct)
          self.payment(coin, productName, productValue)
       else:
          # 잘못된 값을 입력받으면 에러 메시지를 출력하고 제품선택 메뉴로 이동한다. 
          print(texts.select_fault)
          self.selectProduct(coin)


    def getProductValue(self, product):
        returnValue = 0
        for selection, value  in Product.productValue.items():
            if selection == product:
                returnValue = value

        return returnValue

    def getProductName(self, product):
        for selection, name  in Product.productType.items():
            if selection == product:
                return name

    def payment(self, coin, name, value):
        coinValue = coin * PRICE_UNIT
        if coinValue >= value:
           balance = coinValue - value
           print(texts.product_out %(name ,int(balance)))
        else:
           print(texts.n_enough_coin %int(coinValue))
        # 지불을 마치면 초기 메뉴로 이동한다.           
        self.run()


#과자 클래스는 커피 클래스를 상속받는다  
class BreadVM(BeverageVM):
    _name = "빵"
 
    def __init__(self):
       # Product 제품 종류, 가격을 Overriding 한다.
       Product.productType = {"1":"소시지빵", "2":"크림빵", "3": "피자빵"}
       Product.productValue = {"1":1500 , "2":1000, "3":2000}
       # 사용자가 자판기 종류를 선택하면 _name 출력한다.
       print( texts.title %self._name)
       
################################################################################

if __name__ == '__main__':

    print("1:음료수 , 2:빵")
    select_vm = input("구동할 자판기를 선택하세요.").strip()
    
    if select_vm == "1":
        vm = BeverageVM()
    
    elif select_vm == "2":
        vm = BreadVM()
    
    else:
        print("잘 못 누르셨습니다. 다시 실행 해 주세요.")
        sys.exit(-1)

    try:
        vm.run()

    except KeyboardInterrupt as exc:
        print("판매를 종료합니다.")
