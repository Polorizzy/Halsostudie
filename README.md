# Hälsostudie – Dataanalys med Python

## Om projektet

Detta projekt går ut på att utforska och analysera hälsodata med hjälp av Python. Syftet är att undersöka olika hälsorelaterade variabler, identifiera mönster i datamaterialet och använda statistiska metoder för att dra slutsatser.

Projektet innehåller både beskrivande statistik, datavisualisering och statistiska analyser.

## Dataset

Datasetet innehåller 800 observationer och följande variabler:

| Variabel | Beskrivning |
|---|---|
| `id` | Unikt ID för varje observation |
| `age` | Ålder |
| `sex` | Kön |
| `height` | Längd |
| `weight` | Vikt |
| `systolic_bp` | Systoliskt blodtryck |
| `cholesterol` | Kolesterolvärde |
| `smoker` | Rökstatus |
| `disease` | Förekomst av sjukdom |

## Genomförd analys

Projektet innehåller följande analysmoment:

### 1. Datainspektion och förberedelse
- Inläsning av datasetet.
- Undersökning av datatyper och datasetets struktur.
- Kontroll av saknade värden och dubbletter.

### 2. Beskrivande statistik
- Beräkning av medelvärde, median, standardavvikelse, minimum och maximum.
- Undersökning av ålders-, vikt-, längd- och blodtrycksfördelningar.
- Analys av kön, rökstatus och sjukdomsförekomst.

### 3. Datavisualisering
- Histogram för numeriska variabler.
- Diagram för kategoriska variabler.
- Visualisering av fördelningar och mönster i datasetet.

### 4. Simulering av sjukdomssannolikhet
- Beräkning av sjukdomsförekomsten i datasetet.
- Simulering med hjälp av binomialfördelningen.
- Jämförelse mellan den faktiska och simulerade sjukdomsförekomsten.

### 5. Konfidensintervall
- Beräkning av ett 95-procentigt konfidensintervall för medelvärdet av det systoliska blodtrycket.

### 6. Hypotesprövning
- Jämförelse av systoliskt blodtryck mellan rökare och icke-rökare.
- Användning av Welch's t-test.
- Undersökning av hypotesen att rökare har ett högre genomsnittligt systoliskt blodtryck.

## Resultat

Några av resultaten från analysen:

- Datasetet innehåller 800 observationer utan saknade värden.
- 5,875 % av observationerna har registrerad sjukdomsförekomst.
- Det beräknade medelvärdet för systoliskt blodtryck är cirka 149,18.
- 95-procentigt konfidensintervall för systoliskt blodtryck är cirka 148,29–150,07.
- Welch's t-test gav ett p-värde på 0,3264. Resultatet ger inte tillräckligt statistiskt stöd för att rökare har ett högre genomsnittligt systoliskt blodtryck än icke-rökare vid signifikansnivån 0,05.

## Tekniker och bibliotek

Projektet är utvecklat med Python och följande bibliotek:

- **Pandas** – Datahantering och analys.
- **NumPy** – Numeriska beräkningar och simuleringar.
- **Matplotlib** – Datavisualisering.
- **SciPy** – Statistiska tester.
- **Jupyter Notebook** – Interaktiv analys och presentation.

## Projektstruktur

```text
Hälsostudie/
│
├── Data/
│   └── health_data.csv
│
├── notebook/
│   └── health_analysis.ipynb
│
├── src/
│   ├── __init__.py
│   ├── analysis.py
│   ├── data_loader.py
│   └── visualization.py
│
├── .gitignore
└── README.md
```

## Syfte och lärdomar

Projektet har gett möjlighet att arbeta praktiskt med dataanalys, Python-programmering, statistiska metoder och visualisering av data.

Målet har varit att använda programmering för att undersöka ett datamaterial, presentera resultat på ett tydligt sätt och dra statistiskt underbyggda slutsatser.