class Money_Box:
    def __init__(self):
        self.coins = 0
        self.dollar_bills = {
            1: 0,
            5: 0,
            10: 0,
        }

    def add_money(self, coin, dollar_bill):
        def add_bill(bill):
            value, ammount = bill
            return self.dollar_bills[value] + ammount

        self.coins += coin
        self.dollar_bills = list(map(add_bill, dollar_bill.items()))

    def print_report(self):
        print(self.coins)
        print(self.dollar_bills)