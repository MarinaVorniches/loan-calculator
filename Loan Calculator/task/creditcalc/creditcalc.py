from math import ceil, floor
from math import log
from math import pow
import argparse

parser = argparse.ArgumentParser(description="Loan calculator")

parser.add_argument("-t", "--type", choices=["diff", "annuity"], required=True,
                    help="You need to choose between two options.")
parser.add_argument("-pt", "--payment", type=float,
                    help='Add payment amount if loan type is "annuity".')
parser.add_argument("-p", "--principal", type=float,
                    help="Add loan principal if needed.")
parser.add_argument("-ps", "--periods", type=int,
                    help="Add number of periods if needed.")
parser.add_argument("-i", "--interest", type=float,
                    help="Add number of periods if needed.")

args = parser.parse_args()
var = [args.type, args.payment, args.principal, args.periods, args.interest]
none_count = 0
neg = 0
j = 0
m_pay = var[1]
principal = var[2]
months = var[3]
if var[4] is not None:
    interest = float(var[4] / (12 * 100))

for j in range(1, 5):
    if var[j] is None:
        none_count += 1
        j += 1
    elif float(var[j]) < 0:
        j += 1
        neg += 1

if (len(var) - none_count) != 4 or neg > 0:
    print("Incorrect parameters")
    exit()


def diff_calc():
    for_over = 0
    for m in range(1, months + 1):
        d_pay = ceil(principal / months + interest * (principal - (principal * (m - 1) / months)))
        for_over += d_pay
        print(f"Month {m}: payment is {d_pay}")
    overpay = round(for_over - principal)
    print()
    print(f'Overpayment = {overpay}')


def ann_calc():
    global principal
    if m_pay is None:
        an_pay = ceil((principal * interest * pow((1 + interest), months)) / ((pow((1 + interest), months)) - 1))
        overpay = ceil(an_pay * months - principal)
        print(f"Your annuity payment = {an_pay}!")
        print(f'Overpayment = {overpay}')
    elif principal is None:
        principal = floor(m_pay / ((interest * pow((1 + interest), months)) / ((pow((1 + interest), months)) - 1)))
        print(f'Your loan principal = {principal}!')
        overpay = round(m_pay * months - principal)
        print(f'Overpayment = {overpay}')
    elif months is None:
        n = ceil(log((m_pay / (m_pay - interest * principal)), (1 + interest)))
        year = n // 12
        month = n % 12
        if year == 0:
            if month == 1:
                print(f'It will take {month} month to repay this loan!')
            else:
                print(f'It will take {n} months to repay this loan!')
        elif year == 1:
            if month == 0:
                print(f'It will take {year} year to repay this loan!')
            elif month == 1:
                print(f'It will take {year} year and {month} month to repay this loan!')
            else:
                print(f'It will take {year} year and {month} months to repay this loan!')
        else:
            if month == 0:
                print(f'It will take {year} years to repay this loan!')
            elif month == 1:
                print(f'It will take {year} years and {month} month to repay this loan!')
            else:
                print(f'It will take {year} years and {month} months to repay this loan!')
        overpay = round(m_pay * n - principal)
        print(f'Overpayment = {overpay}')


if var[0] == 'diff':
    diff_calc()
elif var[0] == 'annuity':
    ann_calc()
else:
    print("Pam-pam")
