# Bank Account #

Den här uppgiften går ut på att skriva en klass för att hantera bankkonton.

## Bedömningsmatris ##

## Planering ##

| Förmåga                           | E                                                                                                                                 | C | A |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Design                            | Med viss säkerhet analyserar du uppgiften och designar ditt program |    | Som för E, men med säkerhet, och du motiverar dessutom utförligt dina val |
| Klassdiagram                      | Du planerar uppgiften med enkla klassdiagram |    |   |

## Kodning och dokumentering ##

| Förmåga                           | E                                                                                                                                 | C | A |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Strukturering                     | Din kod är delvis strukturerad | Din kod är i stor utsträckning strukturerad | |
| Kodningsstil                      | Du använder en konsekvent kodningsstil  för klasser, moduler, metoder, variabler, kommentarer och dokumentation | | |
| Namngivning                       | Du använder en tydlig namngivning i din kod | | |                                         
| Dokumentering                     | Din kod är delvis dokumenterad|   | Du dokumenterar utförligt dina klasser och metoder

## Felsökning ##

| Förmåga                           | E                                                                                                                                 | C | A |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Typsäkerhet                       | Du uppmärksammar problem med typsäkerhet | | |
| Felsökning                        | Du felsöker enkla syntaxfel | Som för E, men effektivt, och dessutom även körtidsfel och programmeringslogiska fel | Som för C, men du använder dig av tester för att systematiskt och effektivt upptäcka och förhindra fel |

## Slutrestultat och Uppföljning ##

| Förmåga                           | E                                                                                                                                 | C | A |
|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|---|---|
| Komplexitet                       | Det färdiga programmet är av enkel karaktär, fungerar tillfredsställande, och är stabilt och robust  | Som för E, men av lite mer avancerad karaktär | Som för C, men programmet är av komplex karaktär, följer SOLID, och fungerar väl |
| Utvärdering                       | Du utvärderar, med enkla omdömen, programmets prestanda och funktionalitet | Som för E, men nyanserade omdömen | Som för C, men du ger även förslag på förbättringar | 

## Uppgiftsbeskrivning ##

Du har blivit inhyrd för att skriva den del av mjukvaran i ett banksystem som hanterar bankkonton.

Du skall skriva en klass: `BankAccount`.

`BankAccount` skall ha en konstruktor som tar ett kontonr, och ett initalsaldo som argument. 

Eftersom det är viktigt saldot på ett konto inte får modifieras hur som helst måste klassen använda encapsulation.

Klassen skall ha en getter (`balance`) som returnerar det aktuella saldot på kontot.

Klassen skall också ha två metoder för att sätta in och ta ut pengar från kontot: `deposit` och `withdraw`. Båda tar `amount` som argument. Saldot på kontot får bara modifieras genom dessa två metoder.

### Exempel ###

#### Python ####

```python
    account = BankAccount(account_number=1, balance=1080
    account.balance >>> 1080
    account.balance = 1337 >>> ERROR
    account.deposit(amount=257)
    account.balance >>> 1337
    account.widthdraw(amount=1295)
    account.balance >>> 42
```

## Genomförande ##

### Versionshantering ###

Gör en `fork` av repot. Klona sen ner till din dator. Kom ihåg att checka in dina ändringar och synka med GitHub.

### Kodning ###

Programmet skall utvecklas med hjälp av testerna.

#### Testning ####

Skapa klassen i `lib/bank_account.py

Testerna finns i `test/bank_account_test.py`

Kör `nosetests test\bank_account_test.py` för att köra testerna.

### Resurser ###

* [Learn Python The Hard Way - Exercise 40: Modules, Classes, and Objects - A First Class Example](http://learnpythonthehardway.org/book/ex40.html#a-first-class-example)
* [What's the point of properties in Python?](http://blaag.haard.se/What-s-the-point-of-properties-in-Python/)
* [Properties vs. Getters and Setters](http://www.python-course.eu/python3_properties.php)
* [Learn Python The Hard Way - Exercise 41: Learning To Speak Object Oriented](http://learnpythonthehardway.org/book/ex41.html)
