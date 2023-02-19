import argparse
import math
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--type")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()
if len(sys.argv) < 5:
    print("Incorrect parameters")
    sys.exit()
elif args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
    sys.exit()
elif args.type == "diff" and args.payment is not None:
    print("Incorrect parameters")
    sys.exit()
elif args.interest is None:
    print("Incorrect parameters")
    sys.exit()
elif (args.interest is not None and float(args.interest) < 0) or (args.payment is not None and float(args.payment) < 0)\
        or (args.principal is not None and int(args.principal) < 0) or \
        (args.periods is not None and int(args.periods) < 0):
    print("Incorrect parameters")
    sys.exit()
else:
    pass


if args.type == "annuity":
    if args.principal is not None and args.periods is not None and args.interest is not None:
        loan_principle = int(args.principal)
        periods_number = int(args.periods)
        loan_interest = float(args.interest)
        interest_rate = loan_interest / (12 * 100)
        monthly_payment = math.ceil(loan_principle * (interest_rate * math.pow((1 + interest_rate), periods_number)) /
                                    (math.pow((1 + interest_rate), periods_number) - 1))
        overpayment = int(monthly_payment * periods_number - loan_principle)
        print(f"Your annuity payment = {monthly_payment}!")
        print(f"Overpayment = {overpayment}")
    elif args.payment is not None and args.periods is not None and args.interest is not None:
        annuity_payment = float(args.payment)
        periods_number = int(args.periods)
        loan_interest = float(args.interest)
        interest_rate = loan_interest / (12 * 100)
        loan_principle = math.floor(annuity_payment / (interest_rate * math.pow((1 + interest_rate), periods_number) /
                                                  (math.pow((1 + interest_rate), periods_number) - 1)))
        overpayment = int(annuity_payment * periods_number - loan_principle)
        print(f"Your loan principal = {loan_principle}!")
        print(f"Overpayment = {overpayment}")
    else:
        loan_principle = loan_principle = int(args.principal)
        monthly_payment = float(args.payment)
        loan_interest = float(args.interest)
        interest_rate = loan_interest / (12 * 100)
        months_number = math.ceil(
            math.log(monthly_payment / (monthly_payment - interest_rate * loan_principle), 1 + interest_rate))
        years, months = divmod(months_number, 12)
        if years > 1:
            years_str = f"{years} years"
        else:
            years_str = f"{years} year1"
        if months > 1:
            months_str = f"{months} months"
        else:
            months_str = f"{months} month"
        if years != 0 and months != 0:
            print(f"It will take {years_str} and {months_str} to repay this loan!")
        elif years == 0:
            print(f"It will take {months_str} to repay this loan!")
        else:
            print(f"It will take {years_str} to repay this loan!")
        overpayment = int(monthly_payment * months_number - loan_principle)
        print(f"Overpayment = {overpayment}")

if args.type == "diff":
    loan_principle = int(args.principal)
    periods_number = int(args.periods)
    loan_interest = float(args.interest)
    interest_rate = loan_interest / (12 * 100)
    sum_payment = 0
    for i in range(periods_number):
        monthly_payment = math.ceil(loan_principle / periods_number + interest_rate * (loan_principle - loan_principle *
                                                                                       i / periods_number))
        sum_payment += monthly_payment
        print(f"Month {i+1}: payment is {monthly_payment}")
    overpayment = int(sum_payment - loan_principle)
    print(f"Overpayment = {overpayment}")
