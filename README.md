# Aristotle's Key Key Words

From Greg Crane:

> Bywater 1911 states that methodos is "a favourite word of Aristotle."

> To what extent is that true?


## Comparisons with Plato

### total tokens

- Plato: 576,941
- PerseusDL Aristotle: 318,517
- 1st1KGreek Aristotle: 737,435

### total lemmata

- Plato lemmata: 15,514
- PerseusDL Aristotle lemmata: 10,494
- First1KGreek Aristotle lemmata: 35,047

### parts per million tokens

- Plato: methodos: 46.36804457039115 | arete: 1062.8982524597357 | philia: 176.55524663341245
- PerseusDL Aristotle: methodos: 108.34236186348862 | arete: 2163.6606972149643 | philia: 889.0446752915684
- First1KGreek Aristotle: methodos: 40.196618890113925 | arete: 422.0644983461963 | philia: 175.14241087835353

### Dispersion

#### Plato

|   contains_methodos   |   contains_arete  |	contains_philia |
|-----------------------|-------------------|-------------------|
|    {true,23}	        |   {true,311}	    |   {true,73}       |
|    {false,1739}       |	{false,1451}	|   {false,1689}    |

#### PerseusDL Aristotle

|   contains_methodos   |   contains_arete  |	contains_philia |
|-----------------------|-------------------|-------------------|
|    {true,30}	        |   {true,236}	    |   {true,71}       |
|    {false,2474}       |	{false,2268}	|   {false,2433}    |

#### 1st1KGreek Aristotle

|   contains_methodos   |   contains_arete  |	contains_philia |
|-----------------------|-------------------|-------------------|
|   {true,23}           |	{true,129}      |  	{true,74}       |
|   {false,3993}        |	{false,3887}    |	{false,3942}    |

### Zipf scale

> A fairly recently suggested improvement to such frequencies is the Zipf scale (van Heuven et al., 2014), another measure aiming at making frequencies from different corpora more comparable. (Gries 2023, p. 82)

- Plato Zipf Scale (see Gries 2023, p. 82): methodos: 4.6662187812485 | arete: 6.026491693017919 | philia: 5.246880627875232
- PerseusDL Aristotle Zipf Scale (see Gries 2023, p. 82): methodos: 5.0347982989740885 | arete: 6.335189156212334 | philia: 5.9489235852054305
- 1st1KGreek Aristotle Zipf Scale (see Gries 2023, p. 82): methodos: 4.604189524250612 | arete: 5.62537882332055 | philia: 5.2433913235831415
