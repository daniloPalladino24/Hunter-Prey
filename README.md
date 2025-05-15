# Hunter and Prey

Un gioco arcade 2D sviluppato con Python e Pygame dove due giocatori si sfidano alternandosi nei ruoli di cacciatore e preda.

## Descrizione

Hunter and Prey è un gioco multiplayer locale dove i giocatori si sfidano in tre fasi di gioco:
1. **Fase 1:** Il Giocatore 1 è il cacciatore e il Giocatore 2 è la preda
2. **Fase 2:** I ruoli si invertono, il Giocatore 2 diventa cacciatore e il Giocatore 1 la preda
3. **Deathmatch (opzionale):** In caso di parità, entrambi i giocatori diventano cacciatori in una fase finale all'ultimo sangue

Il gioco utilizza controlli diversi per ciascun giocatore e include effetti sonori, animazioni di movimento e un sistema di punteggio.

## Caratteristiche

- **Modalità a turni:** I giocatori si alternano nei ruoli di cacciatore e preda
- **Grafica pixel art:** Sprite animati per movimento a destra e sinistra
- **Sistema di punteggio:** +10 punti per ogni colpo andato a segno
- **Deathmatch:** Modalità speciale in caso di parità
- **Sistema di proiettili:** Fino a 3 proiettili contemporanei per giocatore
- **Barra di salute condivisa:** Durante il deathmatch
- **Input personalizzati:** Nomi giocatori all'inizio della partita
- **Effetti sonori e musica di sottofondo**

## Requisiti

- Python 3.x
- Pygame
- Font: Lobster-Regular.ttf, Montserrat-Regular.ttf (inclusi nella cartella fonts)

## Installazione

1. Clona il repository o scarica i file di progetto
   ```
   git clone https://github.com/daniloPalladino24/hunter-and-prey.git
   cd hunter-and-prey
   ```

2. Installa le dipendenze
   ```
   pip install pygame
   ```

3. Avvia il gioco
   ```
   python scripts/main.py
   ```

## Struttura del Progetto

```
Hunter and Prey/
├── scripts/                # Codice sorgente
│   ├── main.py            # File principale del gioco
│   ├── assets.py          # Caricamento di immagini e suoni
│   ├── settings.py        # Configurazioni e costanti
│   ├── player.py          # Classe Player e relativi metodi
│   ├── projectile.py      # Gestione proiettili e collisioni
│   └── graphic.py         # Interfaccia grafica e menu
├── media/                  # File multimediali
│   ├── R1.png - R6.png    # Animazioni camminata destra
│   ├── L1.png - L6.png    # Animazioni camminata sinistra
│   ├── DR1.png - DR6.png  # Animazioni demone destra
│   ├── DL1.png - DL6.png  # Animazioni demone sinistra
│   ├── RBS.png, LBS.png   # Sprite fermi
│   ├── DRstanding.png     # Sprite demone fermo destra
│   ├── DLstanding.png     # Sprite demone fermo sinistra
│   ├── bg.png             # Sfondo del gioco
│   ├── menu_background.png # Sfondo del menu
│   ├── bgs.mp3            # Musica di sottofondo
│   └── suono_proiettile.wav # Effetto sonoro proiettile
└── fonts/                  # Font utilizzati
    ├── Lobster-Regular.ttf
    └── Montserrat-Regular.ttf
```

## Comandi

### Giocatore 1
- **Movimento:** A (sinistra), D (destra)
- **Salto:** W
- **Sparo:** SPAZIO

### Giocatore 2
- **Movimento:** Freccia SINISTRA, Freccia DESTRA
- **Salto:** Freccia SU
- **Sparo:** SHIFT DESTRO

## Meccanica di Gioco

1. **Inserimento Nomi:** All'inizio del gioco, i giocatori inseriscono i loro nomi
2. **Prima Fase (50s):** Giocatore 1 (Cacciatore) vs Giocatore 2 (Preda)
3. **Seconda Fase (50s):** Giocatore 2 (Cacciatore) vs Giocatore 1 (Preda)
4. **Risultato:**
   - Se un giocatore ha più punti dell'altro, vince
   - In caso di parità, inizia la fase Deathmatch

### Deathmatch
- Entrambi i giocatori sono cacciatori
- Barra di salute condivisa al centro
- Vince chi riesce a spostare completamente la barra dalla propria parte

## Autori

- Palladino Danilo
- Dedi Vittorio

## Licenza

Questo progetto è distribuito con licenza [MIT](LICENSE).
