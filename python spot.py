# python slot program
import random


def spin_slots():
      symbols = ["🌟", "🍎", "🍌", "👻", "🐪"]
      return [random.choice(symbols) for _ in range(3)]


def spin_print(row):
      print(" | ".join(row))
      return row


def payout(row, bet):
      if row[0] == row[1] == row[2]:
            if row[0] == "🌟":
                  return bet * 5
            elif row[0] == "🍎":
                  return bet * 4
            elif row[0] == "🍌":
                  return bet * 3
            elif row[0] == "👻":
                  return bet * 2
            elif row[0] == "🐪":
                  return bet * 1
      return 0


def main():
      balance = 100
      symbols = ["Symbols:🌟🍎🍌👻🐪"]
      print("*************************************")
      print("Welcome to the Python Slot Machine!")
      print("*************************************")
      print(f"Your available balance is: ${balance:.2f}")
      print(symbols)


      while True:
            print("*************************************")
            bet = input("Enter your bet amount : $").strip()
            if bet.lower() == 'q':
                  print("Thanks for playing!")
                  break
            if not bet.isdigit():
                  print("Invalid bet amount. Please enter a numerical value.")
                  continue
            bet = int(bet)
            if bet > balance:
                  print("Insufficient balance for this bet. Please enter a lower amount.")
                  continue
            if bet <= 0:
                  print("Bet amount must be greater than zero.")
                  continue

            balance -= bet
            print(f"You bet: ${bet:.2f}")
            print(f"Remaining balance: ${balance:.2f}")
            print("spinning...\n")
            row = spin_slots()
            spin_print(row)
            payout_amount = payout(row, bet)
            if payout_amount > 0:
                  print(f"Congratulations! You won: ${payout_amount:.2f}")
            else:
                  print("No win this time. Better luck next spin!")
            balance += payout_amount
            print(f"Updated balance: ${balance:.2f}")
            ask = input("if you want to play again(y/n): ").upper()

            if ask != 'Y':
                print("Thank you for playing!")
                break
            else:
                continue



if __name__ == "__main__":
      main()