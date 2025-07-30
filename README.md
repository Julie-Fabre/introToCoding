### Intro to coding 


## Matlab: Hangman game

Use the `codingIntro.md` script as a template to live code with the in2science students.

With this example you can cover:
- coding window / command window / workspace
- variables
- types of variables (cell, characters, numbers)
- for and while loops
- indexing into variables
- displaying text in the command window
- clearing / re-defining variables

Generating the word bank is an easy and interactive part of the tutorial - be sure to ask for neuroscience / lab related words!

## Python: Game of Live

Use `codingIntro_python.ipybn` for live coding, and `game_of_life.py` as a cool application. The latter uses [pygame](https://www.pygame.org/), which can be installed using the provided conda environment:
```
conda env create --name coding --file environment.yml
```
Next, activate the environment and run the game 
```
conda activate coding
python game_of_life.py
```
For options (available initialisations):
```
python game_of_life.py help
```

Alternatively, run the notebook [online using Binder](https://tinyurl.com/5bc5mrx5). This only works for the notebook, not the game of life script, since it can't launch the popup window. 
