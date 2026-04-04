class payment:
    def process_payment(self):
        print("processing payment")
class creditcard(payment):
    def process_payment(self):
        print("paid using credit card")
class upi(payment):
    def process_payment(self):
        print("paid using upi")
for p in [creditcard(),upi()]:
 p.process_payment()
