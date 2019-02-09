Nel progetto sono presenti i file python e i dati simulati mediante il software 'Hugin educational' necessari a riprodurre i risultati presenti nel file "Relazione Baldrati 6174233.pdf".

Se si vuole riprodurre i risultati presenti nella suddetta relazione dovrà essere eseguito il codice del file test.py.

Le reti bayesiane analizzate sono due, sono state prese dai file di esempio del software Hugin e sono precisamente le reti: "fire.net" e "ChestClinic.net" (presenti anch'esse nel progetto).
Nel progetto sono anche presenti i file "firetables.pdf" e "chestclinictables.pdf" nei quali sono scritte le distribuzioni per le due reti su cui è stato realizzato l'apprendimento.

Se si vuole testare l'apprendimento con altri dati è necessario aprire i file "fire.net" o "ChestClinic.net" mediante il software Hugin e simulare nuovi casi mediante la funzione "Simulates Cases"

Per l'appredimento dei parametri  stato utilizzato l'approccio a massima verosimiglianza descritto in Russel & Norvig 20.2.1 ed è stato utilizzato Laplace smoothing per evitare stime degeneri (mediante pseudo-counter unitari).

Infine la misura di vicinanza tra la distribuzione appresa e quella reale è stata effettuata mediante la divergenza di Kullback-Leibler.
Gli esperimenti sono stati ripetuti per un numero crescente di elementi del dataset.

