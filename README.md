# Att-Göra-Lista

## Projektbeskrivning

Det här projektet är en digital att-göra-lista som är skapad i Python.

Programmet låter användaren:
- Skapa nya uppgifter
- Visa sina uppgifter
- Markera uppgifter som klara
- Ta bort uppgifter
- Skapa en sammanfattning av dagens uppgifter
- Skicka sammanfattningen via Gmail

Uppgifterna sparas i en JSON-fil så att de finns kvar när programmet startas igen.

## Funktioner

Programmet använder:
- Python
- Listor och dictionaries
- JSON
- Filhantering
- Funktioner
- Felhantering
- smtplib för att skicka Gmail

## Installation

För att köra programmet behövs Python.

Installera även biblioteket `python-dotenv`:

```bash
pip install python-dotenv