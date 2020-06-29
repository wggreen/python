purchase_subtotal = 2000 * 40
purchase_commission = purchase_subtotal * 0.03
purchase_total = purchase_subtotal + purchase_commission
sale_subtotal = 2000 * 42.75
sale_commission = sale_subtotal * 0.03
sale_net = sale_subtotal - sale_commission
net_earnings = sale_net - purchase_total
print("Joe paid $", purchase_subtotal, "for the stock")
print("Joe paid the broker $", purchase_commission, "for the purchase")
print("Joe got $", sale_subtotal, "when he sold the stock")
print("Joe paid the broker $", sale_commission, "for the sale")
if net_earnings > 0:
    print("Joe made money!")
    print("Joe made $", net_earnings)
else:
    net_earnings = 0 - net_earnings
    print("Joe lost money")
    print("Joe lost $", net_earnings)

