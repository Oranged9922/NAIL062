# Odpovede k otázkam
## Zoznam pojmov

### 1. Model vo výrokovej logike, pravidvostné funkcie výroku
#### Intuícia
- Model je špecifická interpretácia logických výrokov, ktorá dáva konkrétne hodnoty jednotlivým premenným. Táto interpretácia je daná nastavením hodnôt premenných v rámci daného modelu. Pravidlá logiky, ktoré určujú, aké vzťahy musia existovať medzi hodnotami premenných pre to, aby bol celý výrok pravdivý, sa nazývajú pravdivostné funkcie výroku. Sú definované pre jednotlivé logické operátory a slúžia k hodnoteniu výroku v rámci daného modelu.
- Napríklad pre výrok  "p ∧ q", kde "p" a "q" sú premenné, môžu byť pre tento výrok definované nasledujúce modely:
    - p = True, q = True. V tomto prípade je výrok  "p ∧ q" pravdivý, pretože platí konjunkcia pre pravdivé hodnoty p a q.
    - p = True, q = False. V tomto prípade je výrok "p ∧ q" nepravdivý, pretože platí pravidlo logiky konjunkcia pro pravdivú hodnotu p a nepravdivú hodnotu q.
#### Odpoveď na otázku
- Model jazyka nad $\mathbb{P}$ je ohodnotenie z $^{\mathbb{P}}2$. Trieda všetkých modelov jazyka nad $\mathbb{P}$ sa značí $M(\mathbb{P})$, teda $M(\mathbb{P})=^\mathbb{P}2$. Výrok $\varphi$ nad $\mathbb{P}$ (je):
    - **platí** v modeli $\upsilon \in M(\mathbb{P})$, pokiaľ $\overline{\upsilon}(\varphi) = 1$. Potom $\upsilon$ je model výroku $\varphi$,
    - **pravdivý** ((logicky) platí, tautológia), ak platí v každom modeli jazyka, značíme |$= \varphi$.
    - **lživý** (sporný), ak nemá model,
    - **nezávislý**, ak platí v nejakom modeli a neplatí v inom,
    - **splniteľný**, pokiaľ má model
- Výroky $\varphi$ a $\psi$ sú (logicky) **ekvivalentné**, píšeme $\varphi\sim\psi$, ak majú rovnaké modely.

### 2. Sémantické pojmy (pravdivosť, lživosť, nezávislosť, splniteľnosť) v logike vzhľadom k teórii
#### Intuícia
- Sémantické pojmy dávajú význam logickým výrokom a ich interpretácii.
    - Pravdivosť: stav, kedy logický výrok odpovedá skutočnosti. Pravdivosť výrokov možno hodnotiť v rámci rôznych modelov, kde sa premenným priradzujú konkrétne hodnoty.
    - Lživosť: stav, kedy logický výrok nesplňuje skutočnosť. Hodnotíme v rámci rôznych modelov.
    - Nezávislosť: znamená, že hodnota jedného výroku nie je závislá na hodnote iného výroku.
    - Splniteľnosť: existuje model, v ktorom je daný výrok pravdivý.
#### Odpoveď na otázku
- Nech $T$ je teória nad $\mathbb{P}$. Výrok $\varphi$ nad $\mathbb{P}$ je
    - **pravdivý** v $T$ (platí v $T$), ak platí v každom modeli $T$, značíme |$= \varphi$, Hovoríme tiež, že $\varphi$ je (sémantickým) dôsledkom teórie $T$.
    - **lživý** v $T$ (sporný v $T$), ak neplatí v žiadnom modeli teórie $T$.
    - **nezávislý** v $T$, ak platí v nejakom modeli teórie $T$ a neplatí v inom.
    - **splniteľný** v $T$, (konzistentný s $T$), ak platí v nejakom modeli $T$.
- Výroky $\varphi$ a $\psi$ sú **ekvivalentné** v $T$ ($T$-ekvivalentné), písané $\varphi\sim_{T}\psi$, ak každý model teórie $T$ je modelom $\varphi$ práve keď je modelom $\psi$.
### 3. Ekvivalencia výrokov, resp. výrokových teórií, T-ekvivalencia
#### Intuícia
- Ekvivalencia výrokov znamená, že dva rôzne výroky majú rovnaký význam alebo majú rovnaký dôsledok. To znamená, že ak je jeden výrok pravdivý, druhý výrok musí byť tiež pravdivý a naopak. Ekvivalencia výrokov je symbolicky označovaná ako "≡".
- T-ekvivalencia je špeicálny druh ekvivalencie medzi logickými teóriami. Znamená, že dve teórie sú ekvivalentné, ak pre každý výrok jednej teórie vieme nájsť ekvivalentný výrok v druhej teórii a naopak. T-ekvivalencia umožňuje porovnávať rôzne teórie a hľadať najefektivnejšiu alebo najvhodnejšiu teóriu pre daný problém.
#### Odpoveď na otázku:
- Výroky $\varphi$ a $\psi$ sú **ekvivalentné** v $T$ ($T$-ekvivalentné), písané $\varphi\sim_{T}\psi$, ak každý model teórie $T$ je modelom $\varphi$ práve keď je modelom $\psi$.
### 4. Sémantické pojmy o teorii (sporná, bezsporná, kompletná, splniteľná)
#### Intuícia
- sporná teória: je teória, ktorá obsahuje protikladné výroky, ktoré nie je možné súčasne považovať za pravdivé.
- bezsporná teória: je teória, ktorá neobsahuje protikladné výroky, teda všetky výroky sú konzistentné.
- kompletná teóia: je teória, ktorá obsahuje dostatočné množstvo pravidiel a axiómov pre rozhodnutie o pravdivosti akéhokoľvek výroku, ktorý je možné v rámci teórie formulovať.
- splniteľná teória: je logická teória, v ktorej existuje aspoň jeden model, ktorý spĺňa všetky axiómy a pravidlá teórie.
#### Odpoveď na otázku
Výroková teória $T$ nad $\mathbb{P}$ je (sémanticky):
- **sporná**, ak v nej platí $\bot$ (spor), inak je **bezsporná** (splniteľná)
- **kompletná**, ak nie je sporná a každý výrok v nej je pravdivý či lživý, t. j. žiadny výrok v nej nie je **nezávislý**.

### 5. Extenzia teórie (jednoduchá, konzervatívna), zodpovedajúce sémantické kritéria
#### Intuícia
- Extenzie teórie sa týkajú rozsahu a zložitosti logickej teórie.
    - jednoduchá teória: je logická teória s čo najmenším počtom axiomov a pravidiel. Jendoduchá teória má menší rozsah a je jednoduchšia na pochopenie a použitie.
    - konzervatívna teória: je logikcá teória, ktorá rozširuje inú teóriu o ďalšie axiomy a pravidlá bez toho, aby ovplyvnila pravdivosť výrokov pôvodnej teórie. Konzervatívna teória má väčší rozsah, ale zároveň zachováva platnosť pôvodnej teórie.
- Sémantické kritéria pre extenziu sú:
    - Konzervatívnosť: konzervatívna teória musí splňovať, že pre každý výrok, ktorý je pravdivý v základnej teórii, platí rovnako tak aj v rozšírenej teórii a naopak.
    - Závislosť: rozšírená teória musí splňovať, že každý výrok v teórii je možné vyjadriť ako kombináciu výrokov základnej teórie a nových axiómov rozšíriteľnej teórie.
#### Odpoveď na otázku
- **extenzia** teórie $T'$ nad $\mathbb{P}'$, ak $\mathbb{P}'\subseteq\mathbb{P}$ a $\theta^{\mathbb{P}'}(T')\subseteq \theta^{\mathbb{P}}(T)$, o extenzii $T$ teórie $T'$ povieme, že je **jednoduchá**, ak $\mathbb{P}=\mathbb{P}'$, a **konzervatívna**, ak $\theta^{\mathbb{P}'}(T')\cap VF_{\mathbb{P}'}$,
- **ekvivalentná** s teóriou $T'$, ak $T$ je extenziou $T'$ a $T'$ je extenziou $T$

Nech $T$ a $T'$ sú teórie nad $\mathbb{P}$. Teória $T$ je (sémanticky):
- bezsporná, práve keď má model,
- kompletná, práve keď má jediný model,
- extenziou $T'$, práve keď $M^\mathbb{P}(T)\subseteq M^\mathbb{p}(T')$,
- ekvivalentná s $T'$, práve keď $M^\mathbb{P}(T)= M^\mathbb{p}(T')$,
### 6. Tablo z teórie, tablo dôkaz
- Tablo je súbor pravidiel pre hodnotenie logických výrokov. Tieto pravidlá sú popísané v tabuľkovej forme, ktorá umožňuje rýchlo a jednoducho hodnotiť výroky.
- Tablo dôkaz obsahuje pravidlá pre prechod medzi jednotlivými krokmi dôkazu a umožňuje tak vyhodnotiť pravdivosť výroku.
- Tablo strom je metóda pre zobrazovanie dôkazov v logike, kde sa dôkaz zobrazuje ako strom. Každý uzol stromu predstavuje jeden krok dôkazu a hlavná vetva stromu je cieľ dôkazu. Vetve na strome predstavujú jednotlivé kroky dôkazu
- Príklad, pre "p ∧ q → r":
- 
                            p ∧ q → r
                              /   
                    p ∧ q         r
                    /    \       /
                  p       q     p ∧ q

### 7. Kanonický model
- Kanonický model v logike je štandardná interpretácia logického systému, ktorá sa používa k hodnoteniu pravdivostných logických výrokov.
- Má niekoľko charakteristík:
    - Je to štandardná interpretácia, ktorá sa používa k hodnoteniu pravdivosti výrokov v danom logickom systéme,
    - Je to model, v ktorom sú všetky formulácie daného logického systému splniteľné,
    - Kanonický model 
- Napríklad pre výrok "p ∨ q" kanonickým modelom môže byť množina všetkých možných sústav elementárnych formulácií {p, q
- Ďalším príkladom je výrok "p → q" kde kanonickým modelom môže byť množina všetkých možných sústav elementárnych formulácií {p, ¬p, q}

### 8. Kongruencia štruktúry, faktorštruktúra, axiomy rovnosti.
- Kongruencie sú relácie medzi prvkami, ktoré sa chovajú ako "rovnosť", ale môžu existovať rozdiely medzi prvkami, ktoré sú kongruentné. 
- Faktostruktura je špecifický druh štruktúry, v ktorej sú prvky rozdelené do skupín tak, aby prvky v rovnakej skupine boli ekvivalentné (tzn. že sa chovajú rovnako v rámci danej štruktúry). Tieto skupiny sa nazývajú faktory a celá štruktúra je faktorštruktúra. Napr. v teórii čísel môže byť definovaná ako relácia medzi číslami, ktorá rozdeľuje čísla na skupiny deliteľných čísel.
- Axiomy rovnosti sú logické výroky, ktoré definujú rovnosť medzi prvkami v algebraickej štruktúre.

### 9. CNF a DNF, Hornov tvar, Množinová reprezentácia CNF, splňujúce ohodnotenie.
- CNF (Conjunctive Normal Form) je reprezentácia logického výrazu pomocou konjunkcií premenných a negácií premenných. DNF (Disjunctive Normal Form) je reprezentácia logického výrazu pomocou disjunkcií premenných a negácií premenných.
- Hornov tvar je špeciálny druh CNF, kde sa v každom klauzuli nachádza maximálne jedna premenná s negáciou.
- Množinová reprezentácia CNF znamená, že logický výraz sa reprezentuje ako množina klauzúl, kde každá klauzula je súbor premenných a negácií premenných.
- Splňujúce ohodnotenie znamená, že danej logickému výrazu je priradená hodnota "pravda" (True).

### 10. Rezolúčne pravidlo, unifikácia, najvšeobecnejšia unifikácia
- Rezolúčne pravidlo je metóda na dedukciu nových vyjadrení z existujúcich vyjadrení v predikátovej logike. Používa sa na vytváranie nových klauzúl z dvoch existujúcich klauzúl tak, že sa z nich odstráni literál, ktorý sa vyskytuje v oboch klauzulách s opačnými predikátmi.
    - Príklad: Dve klauzuly: (A v B) a (¬A v C)
    - Pomocou rezolúčného pravidla odstránime literál A z oboch klauzúl, čo dá novú klauzulu (B v C) 
- Unifikácia je proces, ktorý hľadá ekvivalentné premeny pre dva alebo viac termov tak, aby sa dali zjendotiť do jedného výrazu.
    - Príklad: Hľadáme ekvivalentné premeny pre term F(x,a) a F(b,y)
    - Riešenie: {x/b, y/a}
    - Po aplikovaní týchto premien dostaneme F(b,a), teda zjednotenie termov.
- Najvšeobecnejšia unifikácia (MGU) je najvšeobecnejšie riešenie pre unifikáciu dvoch výrazov.
    - Príklad: Hľadáme MGU pre term F(x,a,b) a F(b,y,z)
    - Riešenie: {x/b, y/a, z/b}
    - Toto je najvšeobecnejšie riešenie pre unifikáciu týchto dvoch termov, pretože obsahuje najväčší počet premien. 
### 11. Rezolúčny dôkaz a zamietnutie, rezolučný strom
- Rezolučný dôkaz je metóda automatického dôkazu v logike, ktorá sa používa na dôkaz konečnosti teórie. Princíp rezolúcie pozostáva z vytvárania nových viet z dvoch pôvodných viet tak, že sa z nich odstráni literál.
- Zamietnutie je proces, ktorý sa používa na dôkaz neplatnosti tvrdenia. V rezolučnom dôkaze sa zamietnutie dosahuje tým, že sa vytvorí rezolúcia, ktorá obsahuje kontradikciu (napr. 0=1).
- Rezolučný strom je grafické zobrazenie rezolučného dôkazu, ktorý zobrazuje ako sa postupne vytvárajú nové vety z pôvodných viet a ako sa konečne dosiahne kontradikcia.

- Príklad rezolučného dôkazu:
    - P: (A v B) --> C
    - ~C
    - Krok 1: A v B
	- Krok 2: ~A
	- Krok 3: B
	- Krok 4: C (z 1. P)
	- Krok 5: Kontradikcia, pretože C je v kroku 2. negované
-
	- Zamietnutie: 
	- P: A --> B
	- ~B
	- Krok 1: A
	- Krok 2: B (z 1. P)
	- Krok 3: Kontradikcia, pretože B je v kroku 2. negované

- Rezolučný strom by mohol vyzerať napríklad takto:

              C
             / 
      (A v B) --> C
             \
              ~C
Kde koreň stromu predstavuje pôvodnú vetu a listy stromu predstavujú nové vety, ktoré vznikli rezolúciou. Kontradikcia sa nachádza na konci stromu.

### 12. Lineárna rezolúcia, lineárny dôkaz, LI-rezolúcia, LI-dôkaz
- varianty rezolúčneho dôkazu, kde sa používajú iba lineárne vety. Lineárnou vetou rozumieme takú vetu, ktorá obsahuje iba jeden negovaný literál. LI-rezolúcia a LI-dôkaz sú varianty lineárnej rezolúcie, kde sa používajú iba lineárne inferencie. Lineárnou inferenciou rozumieme taký dôkaz, ktorý vychádza iba z jednej premennej.
- Príklad lineárnej rezolúcie:
    - P: A --> B
    - ~B
	- Krok 1: A
	- Krok 2: B (z 1. P)
	- Krok 3: ~B
	- Krok 4: Kontradikcia, pretože B a ~B sú v kroku 2 a 3.
 
- Príklad LI-rezolúcie:
	- P: A
	- P: ~A --> B
	- Krok 1: ~A
	- Krok 2: B (z 2. P)
	- Krok 3: Kontradikcia, pretože A a ~A sú v kroku 1.
- Ako vidíme, v príklade lineárnej rezolúcie sa používa iba jedna premenná a v príklade LI-rezolúcie sa používa iba jedna premenná a jedna inferencia.
### 13. Signatúra a jazyk predikátovej logiky, štruktúra daného jazyka
- signatúra je súbor pravidiel a symbolov, ktoré sa používajú v danom jazyku. Signatúra zahŕňa informácie o počte argumentov, ktoré môže predikát mať a o typoch týchto argumentov. Jazyk logiky je jazyk, v ktorom sa používa daná signatúra.
- štruktúra jazyka zahŕňa:
    - predikáty (napr. "je pekný" alebo "je veľký"), ktoré popisujú vlastnosti objektov
    - premenné (napr. "x"), ktoré predstavujú objekty
    - logické spojky ("a", "alebo"), ktoré spájajú predikáty či premenné
    - kvantifikátory, ktoré určujú rozsah platnosti predikátu pre premenné
- príkladom: "(existuje x) (pre každý y) (x je väčší ako y)" - týmto výrokom sa tvrdí, že existuje nejaký objekt x, ktorý je väčší než akýkoľvek iný objekt y.
- ďalší príklad: "(pre každý x) (existuje y) (x a y sú priatelia)" - týmto výrokom sa tvrdí, že pre každý objekt x existuje nejaký objekt y, s ktorým je x priateľom.

### 14. Atomická formule, formule, sentence, otvorené formule
- atomická formule je najjednoduchšia forma výroku v jazyku predikátovej logiky, ktorá sa skladá iba z predikátu a premenných. Atomická formula sa nerozloží na ďalšie formuly.
- formula je výraz v jazyku predikátovej logiky, ktorý môže byť skonštruovaný z atomických formúl pomocou logických spojek a kvantifikátorov.
- sentence je formula, ktorá neobsahuje žiadne neznáme premenné
- otvorená formula je formula, ktorá obsahuje neznáme premenné
- Príklady:
    - atomická formula: "x je veľký", "x je priateľ s y"
    - formula: "(existuje x) (x je veľký ako y)"
    - sentence: "Všetky slony sú veľké"
    - ovorená formula: "x je veľký ako y"
### 15. Instance formule, substitovateľnosť, variant formule
- Instance formuly je formula, ktorá vznikla vložením konkrétnych hodnôt do premenných v pôvodnej formuli.
- Substitúcia je proces vkladania konkrétnych hodnôt do premenných vo formuli.
- variant formuly je formula, ktorá sa líši od pôvodnej formuly iba zmenou pozície premenných alebo ich názvom.
- Príklady:
    - Pôvodná formula: (existuje x)(x je väčší ako y)
    - Instance formuly: (existuje x)(x je väčší ako z)
    - Substitúcia: premenná y sa nahradila premennou z
    - Pôvodná formula: (existuje x)(x je väčší ako y)
    - Variant formuly: (existuje y)(y je väčší ako x) 
### 16. Pravdivostná hodnota formuly v štruktúre pri ohodnotení, platnosť formule v štruktúre 
- pravdivostná hodnota formuly v štruktúre sa určuje ohodnotením premenných v tejto štruktúre. Štruktúra predstavuje konkrétne objekty a ich vlastnosti, ktoré sa používajú na ohodnotenie formuly. Pravdivostná hodnota formuly môže byť pravda alebo nepravda.
- Platnosť formuly v štruktúre znamená, že pre každé ohodnotenie premenných v tejto štruktúre, bude fomrula pravdivá.
- Príklday:
    - Formula: (existuje x)(x je veľký)
    - Štruktúra: {x: slon, y: pes, z: mačka}
    - Pravdivostná hodnota formuly: pravda, pretože pre existuje aspoň jeden objekt x (slon, pes, mačka), ktorý je veľký.
    - Platnosť formuly: platí, pretože pre každé ohodnotenie premenných v tejto štruktúre existuje aspoň jeden objekt, ktorý je veľký.
    - Ďalší príklad:
    - Formula: (pre každý x)(x je slon)
    - Štruktúra: {x: slon, y: pes, z: mačka}
    - Pravdivostná hodnota formuly: pravda, pretože pre každý objekt x (slon, pes, mačka) platí, že x je slon.
    - Platnosť formuly: neplatí, pretože existuje aspoň jeden objekt (y: pes, z: mačka), ktorý nie je slon.
### 17. Kompletná teória v predikátovej logike, elementárna ekvivalencia
- Kompletná teória v predikátovej logike je množina všetkých výrokov, ktoré sú platné pre danú štruktúru. To znamená, že pre každú formulu, ktorá sa dá vyjadriť v danom jazyku, sa dá určiť, či je platná alebo neplatná pre danú štruktúru.
- Elementárana ekvivalencia je vzťah medzi dvoma formulami, ktorý platí, keď pre každú štruktúru platí, že jedna formula je platná iba vtedy, keď je platná aj druhá.
- Príklady:
    - Formula 1: (existuje x)(x je veľký)
    - Formula 2: (existuje y)(y je veľký)
    - Elementárna ekvivalencia: Platí, pretože pre každú štruktúru existuje aspoň jeden objekt, ktorý je veľký, či už sa premenná volá x alebo y
    - Ďalší príklad:
    - Formula 1: (pre každý x)(x je slon)
    - Formula 2: (pre každý x)(~x nie je slon)
    - Elementárna ekvivalencia: Neplatí, pretože pre každú štruktúru existuje aspoň jeden objekt, ktorý nie je slon, takže formula 2 bude mať pravdivosť "nepravda" tam, kde formula 1 bude mať pravdivosť "pravda".
### 18. Podštruktúra, generovaná podštruktúra, expanzia a redukt štruktúry
- Podštruktúra je časť štruktúry, ktorá obsahuje iba určité objekty a ich vlastnosti. 
- Generovaná podštruktúra je podštruktúra, ktorá vzniká iba z objektov a vlastností, ktoré sú nevyhnutné na ohodnotenie konkrétnej formuly.
- Expanzia štruktúry znamená pridanie nových objektov alebo vlastností do štruktúry.
- Redukt štruktúry znamená odstránenie objektov alebo vlastností zo štruktúry.
- Príklad:
    - Štruktúra: {x: slon, y: pes, z: mačka, veľký: {x,y}, malý:{z}}
    - Podštruktúra: {x: slon, y: pes, veľký: {x,y}}
    - Generovaná podštruktúra pre formulu "(existuje x)(x je malý)": {z: mačka, malý:{z}}
    - Expanzia štruktúry: {x: slon, y: pes, z: mačka, w: kôň, veľký: {x,y,w}, malý:{z}}
    - Redukt štruktúry: {x: slon, y: pes, veľký: {x,y}}
### 19. Definovateľnosť v štruktúre
- Definovateľnosť v štruktúre znamená, že pre každý výraz v danom jazyku existuje formula v tom istom jazyku, ktorá ho vyjadruje. To znamená, že pre každý výraz v danom jazyku existuje spôsob, ako ho vyjadriť pomocou formúl v tom istom jazyku.
- Definovateľnosť sa často používa na charakterizáciu jazykov, ktoré sú dostatočne silné na to, aby vyjadrili všetky výrazy v iných jazykoch.
### 20. Extenze o definice
- Extenzia je množina všetkých interpretácií, ktoré spĺňajú danú definíciu. Interpretácia je spôsob, ako priradiť hodnoty objektom a premenným vo formuli, takže sa dá určiť, či je formula pravdivá alebo nepravdivá.
- Extenzia o definície sa často používa na charakterizáciu platnosti formúl v rôznych štruktúrach.
- Príklad:
    - Definícia pojmu "veľký": objekt, ktorý má hmotnosť viac ako 100 kg
    - Extenzia definície pojmu "veľký": množina všetkých interpretácií, kde premenná "x" sa priradí k objektu s hmotnosťou viac ako 100 kg (napr. {x/slon, {x/nosorožec}})
### 21. Prenexná normálna forma, Skolemov variant
- Prenexná normálna forma je štandardný spôsob, ako zapísať formulu v predikátovej logike, pri ktorom sú všetky existenciálne a univerzálne kvantifikátory pred formulou a sú oddelené od ostatných častí formuly. Toto zapísanie umožňuje jednoduchšie porovnanie a manipuláciu s formulami.
- Skolemov variant je variant prenexnej normálnej formy, kde sú všetky existenciálne a univerzálne kvantifikátory nahradené konkrétnymi funkciami. Umožňuje vytvorenie konkrétnej interpretácie.
- Príklad:
    - Formula: (existuje x)(existuje y)(x je veľký a y je malý)
	- Prenexná normálna forma: (existuje x) (existuje y) (x je veľký a y je malý)
	- Skolemov variant: (existuje x) (existuje y) (f(x) je veľký a g(y) je malý), kde f(x) a g(y) sú konkrétne funkcie, ktoré nahrádzajú existenciálne quantifikátory x a y.
### 22. Izomorfizmus štruktúr, izomorfné spektrum, ω-kategorická teória
- Izomorfizmus štruktúr je vzťah medzi dvoma štruktúrami, ktorý znamená, že sú si navzájom kongruentné v tom zmysle, že obsahujú rovnaké objekty a rovnaké vzťahy medzi nimi.
- Izomorfné spektrum je množina všetkých štruktúr, ktoré sú izomorfné s danou štruktúrou.
- omega-kategorická teória sa zaoberá kategóriou izomorfných štruktúr. Rieši otázky týkajúce sa konečnosti a nekonečnosti týchto štruktúr.
- Príklad:
    - Štruktúra A: {x: 1, y: 2, z: 3, vzťah: {(x,y),(y,z)}}
    - Štruktúra A: {a: 1, b: 2, c: 3, vzťah: {(a,b),(b,c)}}
    - Izomorfizmus: existuje funkcia f, ktorá presúva x na a, y na b a z na c a vzťah (x,y) na (a,b) a (y,z) na (b,c)
    - Štruktúry sú izomorfické, pretože obsahujú rovnaké objekty a rovnaké vzťahy medzi nimi.
### 23. Axiomatizovateľnosť, konečná axiomatizovateľnosť, otvorená axiomatizovateľnosť
- Axiomatizovateľnosť je schopnosť teórie alebo jazyka byť opísaný pomocou konečného počtu axióm.
- Konečná axiomatizovateľnosť znamená, že teória alebo jazyk môže byť opísaný pomocou konečného počtu axióm. 
- Otvorená axiomatizovateľnosť znamená, že teória alebo jazyk môže byť opísaný pomocou konečného počtu axióm, alebo pomocou nekonečného počtu axióm, ktoré sú formulované v jazyku teórie alebo jazyku.
- Príklad:
    - Teória euklidovskej geometrie je konečne axiomatizovateľná, pretože môže byť opísaná pomocou konečného počtu axióm. Teória množin ZF je otvorene axiomatizovateľná, pretože mlže byť popísaná pomocou nekonečného počtu axióm, ktoré sú formulované v jazyku teórie množín.
    
### 24. Rekurzívna axiomatizácia, rekurzívna axiomatizovateľnosť, rekurzívne spočetná kompletácia
- Rekurzívna axomomatizácia je proces, pri ktorom sa teória alebo jazyk opisuje pomocou konečného počtu rekurzívne formulovaných axióm. 
- Rekurzívna axiomatizovateľnosť znamená, že teória alebo jazyk môže byť opísaný pomocou konečného počtu rekurzívne formulovaných axióm.
- Rekurzívne spočetná kompletácia je koncept, ktorý sa týka rekurzívne axiomatizovateľných teórií. Táto kompletácia znamená, že teória môže byť kompletne axiomatizovaná pomocou rekurzívnych funkcií a rekurzívnych predpisov.
- Príklad:
    - Teória Peanovej aritmetiky je rekurzívne axiomatizovateľná, môže byť opísaná pomocou konečného počtu rekurzívne formulovaných axióm.
### 25. Rozhodnuteľná a čiastočne rozhodnuteľná teória
- Rozhodnuteľná teória je teória, pre ktorú existuje algoritmus, ktorý umožňuje rozhodnúť, či daná formula je platná v tejto teórii. 
- Čiastočne rozhodnuteľná teória je teória, pre ktorú existuje algoritmus, ktorý umožňuje rozhodnúť, či daná formula je platná v tejto teórii, alebo že formula nie je rozhodnuteľná.

## Zoznam ľahkých otázok
### 1. Množina modelov nad konečným jazykom je možné axiomatizovať výrokom v CNF, výrokom v DNF
-  Množina modelov nad konečným jazykom môže byť axiomatizovaná výrokom v konjunktívnej normalizovanej forme (CNF) alebo v disjunktívnej normalizovanej forme (DNF). CNF znamená, že každý výrok je tvorený konjunkciou (logickým "a") literálov (pravdivostných hodnôt premennej alebo negácie premennej), DNF znamená, že každý výrok je tvorený disjunkciou (logickým "alebo") literálov. Táto metóda nazývaná klonovacie a naznačuje, že každý model môže byť reprezentovaný ako množina literálov, ktoré sú pravdivé v danom modeli.

### 2. Algebra výrokov bezspornej teórie nad konečným jazykom je izomorfná potenčnej algebre
- existuje jedno-k-jedno zobrazenie medzi algebra výrokov bezspornej teórie nad konečným jazykom a potenčnou algebrou, ktoré zachováva vzťahy medzi prvkami v jednej algebre a prvkami v druhej. Izomorfizmus je v matematike vzťah medzi dvoma algebraickými štruktúrami, ktoré sú si navzájom "podobné" a môžu byť jedna druhou premenené jedinečným a bijektívnym zobrazením. Potenčná algebra je špeciálny typ algebry známej ako "potenčná komutatívna algebra" a charakterizuje sa prítomnosťou potencií prvkov.

### 3. 2-SAT, Algoritmus implikačného grafu, jeho korektnosť
- 2-SAT je algoritmus pre riešenie úlohy 2-Satisfiability, ktorá sa týka určenia, či existuje riešenie pre danú množinu logických výrazov v 2-CNF forme (kde každý výraz je konjunkcia dvoch literálov). Algoritmus implikačného grafu je jedným z algoritmov, ktoré sa používajú na riešenie 2-SAT úlohy.

- Algoritmus funguje tým, že vytvorí graf, ktorý sa skladá z dvoch typov uzlov: uzly pre literály a uzly pre výrazy. Literály sú reprezentované ako dva uzly (jeden pre hodnotu "pravda" a jeden pre hodnotu "nepravda") a výrazy sú reprezentované ako dva uzly (jeden pre konjunkciu a jeden pre disjunkciu). Implikačný graf vytvára hrany medzi uzlami, ktoré reprezentujú literály a uzlami, ktoré reprezentujú výrazy, v závislosti na ich vzťahu v danom výraze.

- Algoritmus potom vyhľadáva cyklus v grafe, ktorý obsahuje uzly reprezentujúce oba literály pre jedno a to isté písmeno. Ak taký cyklus nájde, vie, že daná množina výrazov nemá riešenie, pretože by to znamenalo, že literály by boli súčasne pravdivé a nepravdivé. Ak cyklus nenájde, vie, že daná množina výrazov má riešenie.

- Algoritmus implikačného grafu pre 2-SAT je korektný, pretože pre každý prípad, kedy existuje riešenie pre danú množinu výrazov, algoritmus nenájde žiadny cyklus a pre každý prípad, kedy neexistuje riešenie, algoritmus nájde cyklus.

### 4. Horn-SAT, Algoritmus jednotkovej propagácie, jeho korektnosť
- Horn-SAT je algoritmus pre riešenie úlohy Horn-Satisfiability, ktorá sa týka určenia, či existuje riešenie pre danú množinu logických výrazov v Horn-CNF forme (kde každý výraz je konjunkcia literálov a maximálne jeden z nich je negovaný). Algoritmus jednotkovej propagácie je jedným z algoritmov, ktoré sa používajú na riešenie Horn-SAT úlohy.

- Algoritmus funguje tým, že prechádza výrazy v danom vstupe a pre každý výraz, kde existuje jeden literál s hodnotou "pravda", nastaví hodnotu všetkých ostatných literálov v danom výraze na "pravda". Týmto spôsobom algoritmus "propaguje" hodnotu jednotky po výraze a postupne vyrieši celý problém.

- Algoritmus jednotkovej propagácie pre Horn-SAT je korektný, pretože pre každý prípad, kedy existuje riešenie pre danú množinu výrazov, algoritmus nájde riešenie a pre každý prípad, kedy neexistuje riešenie, algoritmus nájde nesplniteľnosť.

- Rovnako ako v prípade 2-SAT, Horn-SAT úloha tiež patrí do kategórie NP-úplnej úlohy, takže algoritmus jednotkovej propagácie pre Horn-SAT nie je počasovo efektívny pre veľké množiny výrazov.
### 5. Algoritmus DPLL pre riešenie SAT
- Algoritmus DPLL (Davis-Putnam-Logemann-Loveland) je algoritmus pre riešenie úlohy SAT (Satisfiability), ktorá sa týka určenia, či existuje riešenie pre danú množinu logických výrazov v CNF (Conjunctive Normal Form) forme.

- Algoritmus DPLL funguje tým, že postupne vyberá literály z daného výrazu a určuje ich hodnotu na "pravda" alebo "nepravda". Týmto spôsobom algoritmus vytvára rôzne kombinácie hodnôt literálov a pre každú kombináciu skúma, či vyhovuje všetkým výrazom v CNF forme. Ak sa algoritmus dostane do stavu, kedy sú všetky výrazy splnené, vie, že daná množina výrazov má riešenie.

- Algoritmus DPLL tiež používa metódy ako unit propagation a pure literal elimination na zefektívnenie vyhľadávania riešení. Unit propagation sa týka dedukcie hodnôt literálov na základe jednotlivých výrazov, ktoré obsahujú iba jedného neznámeho literála. Pure literal elimination sa týka eliminácie literálov, ktoré sa vyskytujú iba v jednom zmysle (buď iba ako kladné alebo iba ako záporné) v celom CNF výraze.

- DPLL algoritmus je korektný, pretože pre každý prípad, keď existuje riešenie pre danú množinu výrazov, algoritmus nájde jedno z možných riešení a pre každý prípad, keď neexistuje riešenie, algoritmus to zistí. Je to jedným z najbežnejšie používaných algoritmov na riešenie SAT problémov.

### 6. Veta o konštantách

### 7. Vlastnosti extenzie o definície

### 8. Vzťah definovateľných množín a automorfizmov
- Definovateľná množina je množina, ktorá sa dá opísať pomocou logických výrazov v danej teórii. Automorfizmus je bijectívna (jedno-na-jedno) funkcia medzi dvoma množinami, ktorá zachováva ich štruktúru.

- V teórii matematickej logiky existuje vzťah medzi definovateľnými množinami a automorfizmami, ktorý sa nazýva Löwenheim-Skolemova veta. Táto veta hovorí, že pre každú teóriu existuje konečná množina modelov, ktorá obsahuje všetky definovateľné množiny teórie a pre každú túto množinu existuje automorfizmus, ktorý prechádza medzi každou definovateľnou množinou a touto konečnou množinou modelov.
### 9. Tablo metóda v jazyku s rovnosťou
- Strom dosiahnutia (reachability tree) je grafické zobrazenie CNF formuly, ktoré zobrazuje vzťahy medzi jednotlivými klauzulami a premennými. Táto metóda sa používa na vyhľadávanie riešení CNF formuly a je veľmi efektívna pre riešenie SAT problémov. Keď je CNF formulá splniteľná, tak existuje cesta v strome dosiahnutia, ktorá prechádza cez všetky klauzuly a pri ktorej sú všetky premenné priradené hodnoty, ktoré formulu splnia. Ak CNF formulá nie je splniteľná, tak neexistuje žiadna cesta v strome dosiahnutia, ktorá by prešla cez všetky klauzuly.
### 10. Veta o kompaktnosti a jej aplikácie

### 11. Veta o korektnosti rezolúcie vo výrokovej logike

### 12. Veta o korektnosti rezolúcie v predikátovej logike

### 13. Súvislosť stromu dosiahnutia a splniteľnosti CNF formule
- Strom dosiahnutia (reachability tree) je grafické zobrazenie CNF formuly, ktoré zobrazuje vzťahy medzi jednotlivými klauzulami a premennými. Táto metóda sa používa na vyhľadávanie riešení CNF formuly a je veľmi efektívna pre riešenie SAT problémov. Keď je CNF formulá splniteľná, tak existuje cesta v strome dosiahnutia, ktorá prechádza cez všetky klauzuly a pri ktorej sú všetky premenné priradené hodnoty, ktoré formulu splnia. Ak CNF formulá nie je splniteľná, tak neexistuje žiadna cesta v strome dosiahnutia, ktorá by prešla cez všetky klauzuly.
### 14. Unifikačný algoritmus (korektnosť)
- Unifikačný algoritmus je metóda, ktorá hľadá unifikáciu medzi dvoma termami. Unifikácia je proces nájdenia rovnakého termu, ktorý môže byť dosiahnutý zmenou premenných v jednom termi na odpovedajúce premenné v druhom termi. Algoritmus sa skladá z dvoch krokov: sústredenie a generalizácia.

- Sústredenie: v tomto kroku sa skúma jednotlivé časti termu a hľadá sa rovnakosť medzi nimi. Ak sa nájde rovnakosť, tieto časti sa zamenia za spoločnú premennú.

- Generalizácia: v tomto kroku sa skúma, či sú premenné, ktoré boli zamenené za spoločnú premennú, kompatibilné s ostatnými časťami termu. Ak áno, tieto premenné sa zmenia na spoločnú premennú.

- Dôkaz korektnosti unifikačného algoritmu zahŕňa ukázať, že ak sa unifikácia uskutoční, tak výsledok bude korektný a unifikácia sa uskutoční len vtedy, keď existuje riešenie.

- Unifikačný algoritmus je korektný, pretože v každom kroku sa vykonáva len jedna zmena a táto zmena sa vykonáva len vtedy, keď je to možné. Ak sa unifikácia uskutoční, tak výsledok bude korektný a unifikácia sa uskutoční len vtedy, keď existuje riešenie. Keď sa unifikácia nedá uskutočniť, tak sa vráti "neunifikovateľný" a algoritmus sa ukončí.
### 15. Neštandardný model prirodzených čísel
- Neštandardný model prirodzených čísel je matematický model, ktorý poskytuje alternatívnu interpretáciu prirodzených čísel. V tomto modely, prirodzené čísla sú interpretované ako množiny a aritmetické operácie sú definované pomocou set-theoretic operácií. Táto interpretácia umožňuje použiť metódy z teórie množín pre riešenie problémov v aritmetike. 
### 16. Kompletné jednoduché extenzie DeLO*

### 17. Existencia spočetného algebraicky uzavreného telesa

### 18. Telesá charakteristiky 0 nie sú konečne axiomatizovateľné
- Je známe, že telesá charakteristiky 0 nie sú konečne axiomatizovateľné. To znamená, že neexistuje konečný zoznam axiomov, ktorý by opisoval všetky telesá charakteristiky 0. Dôvodom je to, že telesá charakteristiky 0 môžu mať nekonečný počet zložiek, ktoré sa nedajú opísať pomocou konečného počtu axiomov.

- Existujú však rôzne spôsoby, ako opísať telesá charakteristiky 0, napríklad pomocou kategórií, kde sa telesá charakteristiky 0 definujú ako kategórie s nekonečným počtom objektov.

### 19. Kritérium otvorenej axiomatizovateľnosti
- Kritérium otvorenej axiomatizovateľnosti je metóda, ktorá slúži na testovanie, či je danej teórie možné axiomatizovať pomocou otvorených formúl. Táto metóda sa zvyčajne využíva v teórii modelov a pozostáva z testovania, či existuje nekonečný rad modelov teórie, ktorý je konečným počtom otvorených formúl. Ak takýto rad existuje, teória sa nazýva otvorene axiomatizovateľná.
### 20. Rekurzívne axiomatizovaná teória je čiastočne rozhodnuteľná, kompletná je rozhodnuteľná
- Rekurzívne axiomatizovaná teória je teória, ktorá je axiomatizovaná pomocou rekurzívne definovanej množiny pravidiel. Čiastočne rozhodnuteľná teória je teória, v ktorej je možné rozhodnúť, či je dany výrok v teórii platný, alebo nie.
- Kompletná teória je teória, kde je možné rozhodnúť o platnosti všetkých výrokov.
- A tak rekurzívne axiomatizovaná teória môže byť čiastočne rozhodnuteľná, ale nie kompletná.
### 21.  Teória konečnej štruktúry v konečnom jazyku s rovnosťou je rozhodnuteľná
- Teória konečnej štruktúry v konečnom jazyku s rovnosťou je rozhodnuteľná, čo znamená, že existuje algoritmus, ktorý pre každú formulu v tejto teórii môže rozhodnúť, či je splniteľná alebo nie. Táto rozhodnuteľnosť je dôsledkom skutočnosti, že teória konečnej štruktúry je rekurzívne axiomatizovaná a konečný jazyk s rovnosťou je čiastočne rozhodnuteľný.
### 22.  Godelové vety o neúplnosti a ich dôsledky (bez dôkazu)
- Tieto vety dokazujú, že pre každú formálnu teóriu, ktorá obsahuje dostatočné množstvo aritmetiky, existujú výroky, ktoré nie je možné ani dokázať, ani vyvrátiť v rámci tejto teórie. Tieto výroky sú teda neúplné.

- Dôsledky týchto vetv sú, že žiadna formálna teória nemôže byť kompletná a konsistentná zároveň, a že existujú v matematike výroky, ktoré sú pravdivé, ale nemôžu byť dokázané v rámci nejakej formálnej teórie

## Zoznam ťažkých otázok
### 1. Veta o korektnosti tablo metódy vo výrokovej logike
- Pre každú teóriu T a formulu phi, ak je phi tablo dokázateľná z T, potom phi je pravdivá v T.
### 2. Veta o korektnosti tablo metódy v predikátovej logike
### 3. Veta o úplnosti tablo metódy vo výrokovej logike
- Pre každú teóriu T a formulu phi, ak je phí pravdivá v T, je tablo dokázateľná z T
### 4. Veta o úplnosti tablo metódy v predikátovej logike
### 5. Veta o konečnosti sporu, dôsledky o konečnosti a systematičnosti dôkazov
### 6. Veta o úplnosti rezolúcie vo výrokovej logike
### 7. Veta o úplnosti LI-rezolúcie pre výrokové Hornove formule
### 8. Veta o úplnosti rezolúcie v predikátovej logike (Lifting lemma)
### 9. Skolemova veta
- Skolemova veta tvrdí, že existuje nekonečný počet rôznych modelov pre každú nekonečnú teóriu v konečnom jazyku.

### 10. Herbrandova veta
- Herbrandova veta hovorí, že pre každú nekonečnú teóriu v konečnom jazyku existuje nekonečný počet rôznych Herbrandových dôkazov pre každú formulku v tejto teórii.
### 11. Lowenheim-Skolemova veta vrátane variatnu s rovnosťou, jej dôsledky
- Lowenheim-Skolemova veta tvrdí, že pre každú nekonečnú teóriu v konečnom jazyku existuje model, ktorý je konečný v počte prvkov. Variacia týchto viet s rovnosťou ukazuje, že existujú rôzne modely pre teórie s rovnosťou, ktoré sú konečné v počte prvkov. Dôsledky týchto viet sú, že nekonečné teórie sú neúplné a že existujú rôzne modely pre tieto teórie, čo umožňuje rôzne interpretácie pre formulky v tejto teórii.
 
### 12. Vzťah izomorfizmu a elementárne ekvivalencie
- Izomorfizmus medzi dvoma matematickými štruktúrami znamená existenciu bijektívnej (jedno-jednoznačnej) a bikontinuálnej (obe-smerne zachovávajúcej) homomorfizmu medzi nimi. Elementárna ekvivalencia znamená, že dve štruktúry sú elementárne ekvivalentné, ak ich elementárne diagramy (diagramy zostavené z elementárnych formúl) sú izomorfické. Vzťah medzi izomorfizmom a elementárnou ekvivalenciou je taký, že dve štruktúry sú izomorfné iba v prípade, že sú aj elementárne ekvivalentné, avšak naopak, dve elementárne ekvivalentné štruktúry nemusia byť nutne izomorfné.
 
### 13. omega-kategorické kritérium kompletnosti
- Omega-kategorické kritérium kompletnosti sa používa na posúdenie, či teória T je kompletná. Týmto kritériom sa posudzuje, či pre každú formulu A existuje dôkaz v T alebo dôkaz v negácii A v T. Ak je táto podmienka splnená, potom T je omega-kompletná. To znamená, že pre každý príklad existuje buď dôkaz alebo dôkaz negácie. Omega-kompletná teória je kompletná, pretože pre každý príklad existuje dôkaz alebo dôkaz negácie.
### 14. Neaxiomatizovateľnosť konečných modelov
- znamená, že pre konečnú množinu modelov nie je možné nájsť konečný počet axióm, ktoré by ich všetky opisovali. Táto skutočnosť sa dá dokázať pomocou Godelovej neúplnosti, ktorá hovorí, že pre každú konsistentnú a dostatočne silnú formálnu teóriu existuje veta, ktorá je v tejto teórii nevypovedateľná. To znamená, že konečný počet axióm nie je schopný opísať všetky modely v rámci konečného jazyka.

### 15. Veta o konečnej axiomatizovateľnosti
- hovorí, že pre každú konečnú teóriu T existuje konečný zoznam axiomat, ktorých kombinácia úplne charakterizuje množinu modelov teórie T. Inými slovami, existuje konečný zoznam pravdivých výrazov, ktorých kombinácia úplne opisuje všetky možné modelové interpretácie danej teórie. Táto veta sa často používa v teórií modelov ako dôkaz toho, že nejaká teória je konečne axiomatizovateľná.
 
### 16. Rekurzívne axiomatizovaná teória s rekurzívne spočetnou kompletáciou je rozhodnuteľná
- znamená, že pre každý vstupný prípad existuje jednoznačný výstup "pravda" alebo "nepravda". Toto vychádza z toho, že rekurzívne axiomatizované teórie môžu byť formulované pomocou rekurzívnych pravidiel a tieto pravidlá sa dajú spočítať. Táto vlastnosť je dôležitá pre formálnu teóriu dedukcie, pretože umožňuje vytvoriť automatické algoritmy pre overovanie platnosti výrokov.

### 17. Nerozhodnuteľnosť predikátovej logiky
-  znamená, že neexistuje algoritmus, ktorý by pre všetky možné formulácie v predikátovej logike mohol jednoznačne určiť, či sú splniteľné alebo nie. Táto neistota má svoj pôvod v Gödelových vietach o neúplnosti, ktoré jasne ukazujú, že pre každú komplexnú formálnu teóriu existujú formulácie, ktoré nemôžu byť jednoznačne označené ako pravdivé alebo nepravdivé.