# Att-Göra-Lista

## Projektbeskrivning

Det här projektet är en digital att-göra-lista som jag har utvecklat med Python. Syftet med programmet är att hjälpa användaren att organisera sina uppgifter och hålla koll på vad som behöver göras och vad som redan är klart.

Programmet körs i terminalen och har en meny där användaren kan välja mellan olika funktioner.

Med programmet kan användaren:
- Lägga till nya uppgifter.
- Visa alla sparade uppgifter.
- Markera uppgifter som klara.
- Ta bort uppgifter.
- Skapa en sammanfattning av dagens uppgifter.
- Skicka sammanfattningen via Gmail.

Uppgifterna sparas automatiskt i en JSON-fil. Det gör att informationen finns kvar även efter att programmet har avslutats och startats igen.

## Funktioner och teknik

Projektet är utvecklat med Python och använder bland annat:

- **Listor och dictionaries:** för att organisera och lagra uppgifterna.
- **JSON:** för att spara och läsa uppgifter från en fil.
- **Filhantering:** för att informationen ska finnas kvar mellan olika programstarter.
- **Funktioner:** för att dela upp koden i olika delar.
- **Felhantering:** för att hantera exempelvis felaktig inmatning.
- **smtplib och EmailMessage:** för att skapa och skicka sammanfattningar via Gmail.
- **python-dotenv:** för att läsa Gmail-inställningar från en separat miljöfil.

## Installation

För att använda programmet behöver du:

1. Installera Python 3.
2. Ladda ner eller klona projektet från GitHub.
3. Öppna projektmappen i exempelvis PyCharm.
4. Installera biblioteket `python-dotenv` genom att skriva följande i terminalen:

```bash
pip install python-dotenv
```

### Gmail-inställningar

För att kunna skicka sammanfattningar via Gmail behöver du skapa en fil som heter `.env` i projektmappen.

Filen ska innehålla följande inställningar:

```text
GMAIL_ADRESS=din@gmail.com
GMAIL_MOTTAGARE=mottagare@gmail.com
GMAIL_APP_LOSENORD=ditt_app_lösenord
```

Ersätt exemplen med dina egna uppgifter. För Gmail behöver du använda ett applösenord.

**Viktigt:** Dela aldrig din riktiga `.env`-fil eller ladda upp den till GitHub. Den innehåller privata inloggningsuppgifter.

## Hur programmet körs

1. Öppna projektet i PyCharm.
2. Kontrollera att filen `todo.py` är öppen.
3. Kör programmet genom att klicka på den gröna körknappen.
4. En meny visas i terminalen.
5. Skriv numret för den funktion du vill använda och tryck på Enter.

### Programmets meny

```text
===== ATT-GÖRA-LISTA =====
1. Lägg till uppgift
2. Visa uppgifter
3. Markera uppgift som klar
4. Ta bort uppgift
5. Dagens sammanfattning
6. Skicka sammanfattningen med mail
7. Avsluta
```

## Exempelbilder

Här kommer skärmbilder som visar hur programmet fungerar.

### 1. Huvudmenyn

<img width="290" height="173" alt="image" src="https://github.com/user-attachments/assets/1830c7dc-01ac-4d54-9486-1bb2a996b8b5" />

### 2. Visa uppgifter

<img width="159" height="96" alt="image" src="https://github.com/user-attachments/assets/a09e19c7-4920-483d-8e7b-569009f25ff5" />

### 3. Dagens sammanfattning

<img width="197" height="132" alt="image" src="https://github.com/user-attachments/assets/673c4334-dd8f-4047-b137-05a96b5cb8f7" />


### 4. Skicka sammanfattning via Gmail

<img width="347" height="342" alt="image" src="https://github.com/user-attachments/assets/ff90ae50-882e-4a83-ba19-a06b2bcbfd37" />

## Projektets filer

- `todo.py` – innehåller programmets kod.
- `uppgifter.json` – sparar användarens uppgifter.
- `.env` – innehåller Gmail-inställningarna och ska hållas privat.
- `.gitignore` – hindrar privata filer från att laddas upp till GitHub.
- `README.md` – beskriver projektet och hur det används.

## Vad jag har lärt mig

Genom det här projektet har jag fått mer erfarenhet av Python och lärt mig hur olika delar av programmering kan användas tillsammans för att skapa ett fungerande program. Jag har bland annat arbetat med listor, dictionaries, funktioner, JSON, filhantering och felhantering.

Jag har också lärt mig hur man kan använda externa bibliotek för att skicka e-post och hur man skyddar känsliga uppgifter med hjälp av en `.env`-fil och `.gitignore`.
