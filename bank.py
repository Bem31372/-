class BankAccount:
    def __inti__(self):
        self.__balance__ = 0

    def deposit(self, amount):
        if amount >0:
            self.__balance__ += amount
            print(f'ฝากสำเร็จ: {amount} บาท')
        else:
            print('ยอดเงินฝากต้อง')
    
    def withdraw(slef,amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"ถอนเงินไม่สำเร็จ: {amount} บาท")
        else:
            print(f"ตอนไม่สำเร็จ:(ยอดเงินไม่เพียงพอต่อการถอน {amount} บาท)")

        def check_balance(self):
            return self.__balance
