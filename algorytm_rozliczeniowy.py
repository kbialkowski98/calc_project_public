from decimal import Decimal

#   Funkcja oblicza najprostszy sposób na rozliczenie grupy osób.
#
#   Args:
#       balances (list of dict): Lista słowników, gdzie każdy słownik
#                                reprezentuje saldo jednej osoby.
#                                Np. [{'name': 'Anna', 'balance': Decimal('-125.00')}]
#
#   Returns:
#       list of str: Lista transakcji do wykonania w formie tekstowej.

def settle_up(balances):
    debtors = [{'name': b['name'], 'balance': abs(b['balance'])} for b in balances if b['balance'] < 0]
    creditors = [b for b in balances if b['balance'] > 0]

    transactions = []

    while debtors and creditors:
        debtor = debtors[0]
        creditor = creditors[0]

        payment_amount = min(debtor['balance'], creditor['balance'])
        payment_amount = round(payment_amount, 2)

        transactions.append(
            f"{debtor['name']} -> {creditor['name']}: {payment_amount:.2f} zł"
        )

        debtor['balance'] -= payment_amount
        creditor['balance'] -= payment_amount

        if debtor['balance'] == 0:
            debtors.pop(0)
        
        if creditor['balance'] == 0:
            creditors.pop(0)

    return transactions

example_balances = [
    {'name': 'Celina', 'balance': Decimal('300.00')},
    {'name': 'Anna', 'balance': Decimal('-125.00')},
    {'name': 'Bartosz', 'balance': Decimal('-175.00')},
    {'name': 'Ewa', 'balance': Decimal('900.00')},      
    {'name': 'Iwona', 'balance': Decimal('-300.00')},   
    {'name': 'Kamil', 'balance': Decimal('-700.00')},           
    {'name': 'Piotr', 'balance': Decimal('200.00')},        
    {'name': 'Kacper', 'balance': Decimal('-100.00')},
]

final_transactions = settle_up(example_balances)

print("Aby się rozliczyć, wykonaj następujące przelewy:")
for t in final_transactions:
    print(f"- {t}")