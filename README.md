# Grammatica Klingon con Parsing CKY

### Indice

- [Descrizione del Progetto](#descrizione-del-progetto)
- [Indice](#indice)
- [Contenuti](#contenuti)
- [Requisiti e Dipendenze](#requisiti-e-dipendenze)
- [Utilizzo](#utilizzo)
- [Componenti del gruppo](#componenti-del-gruppo)
- [Note Aggiuntive](#note-aggiuntive)
- [Task 1.A: Parser CKY](#task-1a-parser-cky)
- [Task 1.B: CKY su grammatica L1 di Jurafsky](#task-1b-cky-su-grammatica-l1-di-jurafsky)
- [Task 1.C: Grammatica Klingon](#task-1c-grammatica-klingon)
- [Task 1.D (extra): Grammatica Klingon con semantica](#task-1d-extra-grammatica-klingon-con-semantica)

## Descrizione del Progetto
Questo progetto si concentra sull'implementazione dell'algoritmo di parsing sintattico CKY per la grammatica della lingua Klingon. L'obiettivo principale è analizzare frasi nella lingua Klingon utilizzando un approccio basato su regole grammaticali e generare alberi sintattici per comprendere la struttura delle frasi.

## Contenuti
Il progetto è strutturato nel seguente modo:

1. **Implementazione CKY:** Contiene il codice Python che implementa l'algoritmo CKY per il parsing sintattico.
2. **Grammatica L1 di Jurafsky:** Utilizzata come prima fase di test per l'algoritmo CKY.
3. **Grammatica Klingon:** Contiene le regole grammaticali per la lingua Klingon, scritte seguendo una notazione formale per il parsing CKY.
4. **File di Esempio:** Includerà frasi in Klingon che verranno analizzate utilizzando l'algoritmo CKY.

## Requisiti e Dipendenze
- Python (versione X.X)
- Altre dipendenze o librerie (se presenti)

## Utilizzo
1. **Setup:** Assicurati di avere Python installato sul tuo sistema.
2. **Esecuzione:** Esegui il file principale che avvia l'algoritmo CKY passando come input le frasi in Klingon da analizzare.
  ```
  python main.py frase_klingon.txt
  ```
  Sostituisci `frase_klingon.txt` con il nome del file contenente la frase in Klingon da analizzare.

## Componenti del gruppo
- **Gianluca Barmina** 884084
- **Marco Amato** 882348

## Note Aggiuntive
- La grammatica Klingon può non essere completa e potrebbe richiedere ulteriori regole per coprire una vasta gamma di frasi.
- Assicurati di avere una conoscenza approfondita della lingua Klingon per definire correttamente le regole grammaticali.

---

## Task 1.A: Parser CKY

La versione di CKY implementata è quella non-probabilistica e rule-based.
L'input consiste in
  - Una frase su cui effettuare il parsing
  - Una grammatica context free, a costituenti in Chomsky Normal Form

### Modellazione della frase

La frase è stata modellata come una lista di stringhe, in cui ogni parola è una elemento della lista

### Modellazione della grammatica

La grammatica è stata modellata come una lista di tuple. Ogni tupla è composta da:
  - Una stringa rappresentante la parte sinistra della regola. Questa stringa rappresenta un simbolo non terminale
  - Una lista di stringhe rappresentante la parte destra della regola. Ognuna delle stringhe rappresenta un simbolo terminale o non terminale.

La grammatica fornita è in formato CNF, quindi:
  - Ogni tupla ha una lunghezza di 1 o 2
  - Se la lunghezza è 2, allora la tupla è nella forma `(A, [B, C])`, dove `A`, `B` e `C` sono simboli non terminali
  - Se la lunghezza è 1, allora la tupla è nella forma `(A, [b])`, dove `A` è un simbolo non terminale e `b` è un simbolo terminale
  - E' ammessa solo la ricorsione a sinistra

### Algoritmo CKY

L'obiettivo dell'algoritmo è quello di creare una struttura sintattica per la frase fornita in input.
Il successo dell'algoritmo ci dice due informazioni:
  - Data la grammatica e la frase esiste un albero sintattico che rappresenta quella frase
  - La frase è sintatticamente corretta rispetto alla grammatica data

L'algoritmo sfrutta la programmazione dinamica per riempire una matrice quadrata di dimensione `n x n`, dove `n` è la lunghezza della frase.
Ogni colonna della matrice corrisponde ad una parola della frase.

L'idea fondamentale dell'algoritmo è che data una regola `A -> BC`, possiamo considerare la produzione di destra delimitata da due estremi: `i` e `j`.
A questo punto, possiamo dividere la produzione in due parti, costituite dai due sintagmi: `B` e `C`.
Considerando ciò, esiste una posizione `k` tale che `i < k < j` che divide la produzione in due parti:
  - da `i` a `k` ci sarà `B`
  - da `k` a `j` ci sarà `C`

Sfruttando questa divisione la tabella verrà costruita in modo da avere:
  - Nella posizione `[i][j]` il simbolo non terminale `A`
  - Nella posizione `[i][k]` il simbolo non terminale `B`
  - Nella posizione `[k][j]` il simbolo non terminale `C`

Questo per rappresentare che il sintagma `A` (lungo da `i` a `j`) produce `B` (lungo da `i` a `k`) e `C` (lungo da `k` a `j`)

Mantenendo questa idea si può intuire che le parti sinistre delle regole che producono i terminali (ossia le parole della frase) verranno inserite nella diagonale principale della matrice.
Considerando una regola `A -> b` stiamo dicendo che il sintagma `A` (lungo da `i` a `j`) produce il terminale `b` (lungo da `i` a `j`).
Tuttavia in questo caso sarà prodotta esattamente una parola, che avrà quindi lunghezza 1, ossia `i = j`, e sicuramente non potrà essere ulteriormente divisa.
Dato che ogni posizione della diagonale avrà `i = j`, ogni posizione `[i][j]` conterrà il simbolo non terminale che produce la parola in posizione `j` della frase.


Il riempimento della matrice avviene sfruttando tre indici: `i`, `j` e `k`.
  - `j` rappresenta la colonna della matrice.
  - `i` rappresenta la riga della matrice. Fissata la colonna `j`, `i` viene decrementato scorrendo le posizioni della colonna `j` in ordine decrescente per riempirle.
  - `k` rappresenta la posizione in cui viene divisa la frase. Scorre fra `i` e `j` per trovare la posizione in cui dividere la produzione di destra della regola.

L'algoritmo è strutturato in tre cicli annidati

#### Primo ciclo: j

Il ciclo più esterno scorre le colonne della matrice in modo crescente e ha il compito di riempire la diagonale principale.
In particolare per ogni colonna (ossia per ogni parola della frase) viene controllato se esiste una regola `A -> b` tale che `b` è la parola in posizione `j` della frase.
Se questa esiste allora viene inserito il simbolo non terminale `A` nella posizione `[j][j]` della matrice.
Ossia nell'elemento della diagonale principale che corrisponde alla colonna (parola) `j-esima`.

Essendo i successivi cicli annidati, il riempimento non viene fatto in un colpo solo.
Nel momento in cui ci sono posizioni valide per l'avvio dei cicli successivi, il riempimento della diagonale si ferma si passa al riempimento delle altre posizioni della matrice.
Il riempimento della diagonale proseguirà poi quando i cicli successivi verranno terminati.

<br>

#### Secondo ciclo: i

Il ciclo interno successivo, una volta fissata la colonna `j`, scorre le righe della matrice, partendo dalla diagonale principale e arrivando alla riga `0`.
Il compito del ciclo è di permettere il riempimento delle colonne della matrice.
Ogni colonna viene riempita in modo decrescente partendo dalla fondo (diagonale principale) e arrivando alla riga `0`.

Questo ciclo sfrutta il fatto che la posizione della diagonale principale per la colonna `j`, considerata ogni volta, è `j` stesso, quindi inizialmente `i = j`.

Un'altra funzione fondamentale di questo ciclo è fissare un estremo sinistro della frase dopo che il precedente ha fissato l'estremo destro.
Fissati entrambi, il ciclo successivo potrà scorrere le posizioni intermedie della frase per individuare la presenza di regole che generano la frase definita dagli estremi `i` e `j`.

<br>

#### Terzo ciclo: k
Una volta fissati gli estremi `i` e `j`, il ciclo più interno scorre le posizioni intermedie fra essi per trovare tutte le possibili posizioni `k` in cui dividere la frase.
Ossia individuare i sintagmi della frase (separati in posizione `k`) tali per cui esiste una regola che li genera.

A questo punto stiamo considerando sicuramente sintagmi composti non da singole parole.
Questo perché se fossero singole parole, allora sarebbero già state inserite nella diagonale principale.
Di conseguenza andiamo a considerare solo le regole della forma `A -> BC`, dove `B` e `C` sono simboli non terminali.
Dati gli estremi `i` e `j`, l'obiettivo è individuare tutti valori di `k` tali per cui `i < k < j` ed esista una regola `A -> BC` tale che `B` è nella posizione `[i][k]` e `C` è nella posizione `[k][j]`.
Più in particolare ciò che ci interessa è il non terminale `A`, che verrà inserito nella posizione `[i][j]` della matrice.

Addentrandoci nel codice, in questo ciclo, avendo fissato gli estremi `i` e `j`, e una certa posizione intermedia `k`, si considera ogni regola della grammatica della forma `A -> BC`.
Per ogni regola in particolare chiamiamo `left` la parte sinistra e `right` la parte destra.
Verifichiamo se `left` è presente nella posizione `[i][k]` e se `right` è presente nella posizione `[k][j]`.
Se entrambe le condizioni sono verificate, ciò significa che:
  - Abbiamo trovato una regola che genera la frase definita dagli estremi `i` e `j`
  - Abbiamo trovato la posizione `k` in cui dividere la frase
  - Sappiamo che il primo sintagma della parte destra della regola (ossia `B`) è nella posizione `[i][k]`
  - Sappiamo che il secondo sintagma della parte destra della regola (ossia `C`) è nella posizione `[k][j]`

Considerando ciò, per rappresentare che questa regola produce la frase, inseriamo il simbolo non terminale `A` nella posizione `[i][j]` della matrice.

Ogni volta che per una certa posizione intermedia `k` vengono analizzate tutte le regole ed eventualmente aggiunte alla matrice, il ciclo termina e si passa alla posizione intermedia successiva.
Ogni volta che per un certo estremo sinistro `i` vengono considerate tutte le posizioni intermedie, il ciclo termina e si passa all'estremo sinistro successivo, scorrendo verso `j`.
  - Ciò si traduce nello scorrimento e riempimento della colonna `j-esima` verso l'alto, ossia verso `0`
Ogni volta che per un certo estremo destro `j` vengono considerate tutte le possibilità di estremi sinistri e posizioni intermedie, il ciclo termina e si passa all'estremo destro successivo, scorrendo verso `n-1`.
  - Ciò si traduce nello scorrimento da sinistra a destra delle colonne. Ogni colonna sarà poi considerata dal ciclo successivo.

L'effetto di tutto ciò è che la frase va ad aumentare di grandezza, considerando sempre più parole, tramite lo spostamento dell'estremo destro.
Ugualmente avviene, fissato l'estremo destro, con quello sinistro.

#### Risultato dell'algoritmo

Data una frase ed una grammatica, 'algoritmo effettua con successo il parsing della frase se nella cella `[0][n-1]` della matrice è presente il simbolo non terminale `S` che rappresenta la radice dell'albero sintattico.
La presenza di questo simbolo come anticipato prima indica che la frase è sintatticamente corretta rispetto alla grammatica data e che sia stato trovato un albero sintattico che la rappresenta.
L'albero sintattico può essere ricostruito a partire dalla matrice, partendo dalla cella `[0][n-1]`.

---

NOTA: Nello pseudocodice visto a lezione e presente nel libro di testo, il primo indice delle righe è `0` mentre il primo indice delle colonne è `1`.
Nella nostra implementazione abbiamo scelto per comodità e naturalezza di utilizzare indici che partono da `0` sia per le righe che per le colonne.
Le conseguenti modifiche apportate rispetto allo pseudocodice sono:
  - Il primo ciclo fa scorrere l'indice `j` da `0` (non da `1`) a `n - 1`, dove `n` è la lunghezza della frase
  - Il secondo ciclo fa scorrere l'indice `i` da `j-1` (non da `j-2`) a `0`
  - Il terzo ciclo fa scorrere l'indice `k` da `i` (non da `i+1`) a `j-1`
  - Quando nella tabella si valuta la presenza del secondo sintagma della parte destra della regola (`C`), si utilizza l'indice `k+1` (non `k`)

---

## Task 1.B: CKY su grammatica L1 di Jurafsky

Il primo task su cui è stato eseguita l'implementazione del parser CKY sono state due frasi in lingua inglese.
  - _book the flight through Houston_
  - _does she prefer a morning flight_

La grammatica utilizzata è la grammatica L1 di Jurafsky, ridotta alle componenti necessarie per il parsing delle due frasi.
<br>
In particolare questa grammatica rispetta un requisito fondamentale per poter funzionare con questa tipologia di Parser, ossia l'essere in Chomsky Normal Form. Come descritto nella sezione precedente quindi avrà solo regole che generano due non terminali oppure un singolo terminale, e avrà ricorsione solo a sinistra.

Per ogni frase, l'output prodotto dal parser consiste in una tabella.
<br>
Il punto della tabella su cui porre attenzione è la posizione in alto a destra (`[0][n-1]` dove `n` è la lunghezza della frase).
Per ogni frase la tabella in output presenta il simbolo `S` nella posizione indicata.
Ciò sta a significare che ognuna è quindi sintatticamente corretta rispetto alla grammatica utilizzata.

### Intepretazione della tabella

In questa sezione verrà fatta l'interpretazione di alcune celle della tabella rispetto ad un esempio di applicazione.
Consideriamo la frase _book the flight through Houston_

Il risultato prodotto è il seguente:
```
    ------------- 0 ------------------  -1-     -------- 2 -------      -3-     ------------------ 4 ------------------                              
0|  ['S', 'VP', 'V', 'Nominal', 'Noun']	[]     	['S', 'VP', 'X2']  	[]   	['S', 'VP', 'X2', 'S', 'S', 'VP', 'VP']
1|  []                                 	['Det']	['NP']             	[]   	['NP']                                 
2|  []                                 	[]     	['Nominal', 'Noun']	[]   	['Nominal']                            
3|  []                                 	[]     	[]                 	['P']	['PP']                                 
4|  []                                 	[]     	[]                 	[]   	['NP', 'PN'] 
```
Considerando la seguenti celle:
  - `[3][4]` contenente il simbolo `PP`
  - `[3][3]` contenente il simbolo `P`
  - `[4][4]` contenente il simbolo `NP`

Il `PP` è il sintagma che "produce" la frase dalla posizione `3` alla `4`, di conseguenza si trova nella posizione `[3][4]`.
Esso è composto dal sintagma che "produce" la frase nella posizione `3` (`P`), e quindi nella posizione `[3][3]`, e dal sintagma che "produce" la frase nella posizione `4` (`NP`), e quindi nella posizione `[4][4]`. 

Ovviamente la conoscenza del fatto che `PP` è composto da `P` e `NP` è data dalla grammatica utilizzata.
Ciò significa che nella grammatica sarà presente una regola: `PP -> P NP`.
Quindi un altra interpretazione che può essere fatta è che nella pozione `[3][3]` è contenuto il primo sintagma generato e nella posizione `[4][4]` è contenuto il secondo.
Mentre nella posizione `[3][4]` è contenuta la parte sinistra della regola `S -> VP PP` che genera i due sintagmi.

Considerando ora le seguenti celle:
  - `[2][4]` contenente il simbolo `Nominal`
  - `[2][2]` contenente il simbolo `Nominal`
  - `[3][4]` contenente il simbolo `PP`

Il `Nominal` è il sintagma che "produce" la frase dalla posizione `2` alla `4`, di conseguenza si trova nella posizione `[2][4]`.
Esso è composto dal sintagma che "produce" la frase nella posizione `2` (`Nominal`), e quindi nella posizione `[2][2]`, e dal sintagma che "produce" la frase dalla posizione `3` alla `4` (`PP`), e quindi nella posizione `[3][4]`.

Anche in questo caso la conoscenza del fatto che `Nominal` genera `Nominal` e `PP` è data da una regola presente nella grammatica: `Nominal -> Nominal PP`.
Quindi in `[2][2]` è contenuto il primo sintagma generato, in `[3][4]` il secondo, e unendoli considerando anche le posizioni della frase generate, in `[2][4]` è contenuto il sintagma (parte sinistra della regola) che li genera.

---

Per questa frase, nella posizione `[0][4]` il simbolo `S` è presente tre volte. Ciò significa che per la grammatica data sono possibili tre alberi sintattici distinti che generano la frase (quindi si hanno tre radici possibili).
Una possibilità per distinguere i tre alberi è l'applicazione del backtracking per tenere traccia delle diverse catene di produzioni che portano alla generazione della frase.

Il fatto che poi, oltre ad `S`, in posizione `[0][4]` siano presenti anche altri simboli, come ad esempio `VP`, indica che l'intera frase è generata anche da altri sintagmi, e quindi, per esempio, che la frase stessa sia un `VP`.

---

## Task 1.C: Grammatica Klingon

---

## Task 1.D (extra): Grammatica Klingon con semantica