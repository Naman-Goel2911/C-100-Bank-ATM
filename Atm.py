class ATM(object):
    def __init__(self, cardNumber, pinNumber):
        self.cardNumber = cardNumber
        self.pinNumber = pinNumber
        self.balance = int(0)
    
    def cashWithdrawal(self):
        withdrawAmount = int(input('Enter the amount that you want to withdraw: '))
        self.balance = self.balance - withdrawAmount
        print(f'Successfully withdrew {withdrawAmount}!')

    def cashDeposit(self):
        depositAmount = int(input('Enter the amount that you want to deposit: '))
        self.balance = self.balance + depositAmount
        print(f'Successfully deposited {depositAmount}!')

    def balanceQuery(self):
        print(f'You currently have {self.balance} in your bank account!')


theAtm = ATM(1, 2)
theAtm.cashDeposit()
theAtm.balanceQuery()
