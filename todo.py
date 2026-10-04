import json
import smtplib
import os
from dotenv import load_dotenv
from email.message import EmailMessage

load_dotenv()


def spara_uppgifter():
    with open("uppgifter.json", "w") as fil:
        json.dump(uppgifter, fil)


def dagens_sammanfattning():
    sammanfattning = "===== DAGENS SAMMANFATTNING =====\n"

    for uppgift in uppgifter:
        if uppgift["klar"]:
            symbol = "✔"
        else:
            symbol = "⬜"

        sammanfattning += f"{symbol} {uppgift['namn']}\n"

    sammanfattning += f"\nTotalt: {len(uppgifter)} uppgifter"

    print(sammanfattning)

    return sammanfattning


def skicka_mail():
    sammanfattning = dagens_sammanfattning()

    meddelande = EmailMessage()

    meddelande["Subject"] = "Dagens sammanfattning"
    meddelande["From"] = os.environ["GMAIL_ADRESS"]
    meddelande["To"] = os.environ["GMAIL_MOTTAGARE"]

    meddelande.set_content(sammanfattning)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(
                os.environ["GMAIL_ADRESS"],
                os.environ["GMAIL_APP_LOSENORD"]
            )
            server.send_message(meddelande)

        print("Mejlet skickades!")

    except Exception:
        print("Mejlet kunde inte skickas.")

uppgifter = []

try:
    with open("uppgifter.json", "r") as fil:
        uppgifter = json.load(fil)

except:
    uppgifter = []


while True:
    print()
    print("===== ATT-GÖRA-LISTA =====")
    print("1. Lägg till uppgift")
    print("2. Visa uppgifter")
    print("3. Markera uppgift som klar")
    print("4. Ta bort uppgift")
    print("5. Dagens sammanfattning")
    print("6.Skicka sammanfattningen med mail")
    print("7. Avsluta")

    val = input("Välj: ")

    if val == "1":
        uppgift = input("Skriv en uppgift: ")

        uppgift = {
            "namn": uppgift,
            "klar": False
        }

        uppgifter.append(uppgift)
        spara_uppgifter()

    elif val == "2":

        print("===== DINA UPPGIFTER =====")

        for nummer, uppgift in enumerate(uppgifter, start=1):

            if uppgift["klar"]:
                symbol = "✅"
            else:
                symbol = "⬜"

            print(f"{nummer}. {symbol} {uppgift['namn']}")

    elif val == "3":
        try:
            nummer = int(input("Vilken uppgift är klar?: "))
            uppgifter[nummer - 1]["klar"] = True
            spara_uppgifter()

        except ValueError:
            print("Du måste skriva ett nummer.")

        except IndexError:
            print("Det finns ingen uppgift med det numret.")

    elif val == "4":
        try:
            nummer = int(input("Vilken uppgift vill du ta bort?: "))
            uppgifter.pop(nummer - 1)
            spara_uppgifter()

        except ValueError:
            print("Du måste skriva ett nummer.")

        except IndexError:
            print("Det finns ingen uppgift med det numret.")

    elif val == "5":
        dagens_sammanfattning()

    elif val == "6":
        skicka_mail()

    elif val == "7":
        break