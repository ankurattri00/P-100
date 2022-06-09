class atm(object):
    def __init__(self, card_number,pin_number):
        self.card_number=card_number
        self.pin_number=pin_number

    def CashWithdrawl(self):
        print("CashWithdrawled")

    def BalanceInquiry(self):
        print("BalnceInquired")

axisbank=atm(97648,8937)
print(axisbank.CashWithdrawl())
print(axisbank.BalanceInquiry())
print(axisbank.card_number)
print(axisbank.pin_number)
    
    
    




