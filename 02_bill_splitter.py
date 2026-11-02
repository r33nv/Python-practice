def main():
    bill = float(input("What is your bill? "))
    tip = float(input("how much would you like to tip? "))
    people = float(input("how many people accompany you? "))
    result = split_bill(bill,tip,people)
    print(f"Each member bill should be respectively : {result:,.2f}$")
def split_bill(bill,tip,people):
    tipped = float(tip/100 * bill)
    total = tipped + bill
    each = total / people
    return each
main()