# Quelque note personnelle seron anoté ici

## Ce programe consistera a voir si:

- Sommes nous désagréables lorsqu'il y a beaucoup de personnes autour de nous?
- Les vieux gagnent-ils plus d'argent que les jeunes?

## Ce programme viendra se reposé sur PPLAPI (résau social factice) contenam:

1. un âge
2. une nationalité
3. une position
4. 5 traits de personnalités communs:
    1. Ouverture
    2. Conscienciosité
    3. Extravension
    4. Agréabilité
    5. Neuroticisme

## 3 Concepts / Objets (Batail naval)
(Avec leurs attributs)

1. Le plateau de jeu
    1. Largueur
    2. Hauter

2. Le bateau
    1. Largeur

3. L'agent

## Les étapes de l'analyse et du design orienté objet

1. L'analyse
    1. Definir les grands objets

2. Le Design
    1. Définir les intéractions entre objets
    2. Réaliser le diagramme de séquence

3. La programmation
    1. Réaliser le diagramme de classe
    2. Coder

# (P1C3)

## 2 types de graphiques: 

1. Agréabilité vs Densité de population
2. Age vs Revenus

## Les objets:

Agent
Position
Zone
Graph

## Chaque objet a des atribut et des methodes

Atribut - une proprieter specifique a cette objet.

Methode - c'est une action que peut realiser uniquement cette objet.

Atribut = a:

Methode = m:

### Agent
a: agreeability: Float
a: position: Position
m: initialisation()

### position
a: latitude: Float
a: longitude: Float
m: initialisation()

### Zone
a: corner1: Position
a: corner2: Position
m: initialisation()
m: population()
m: population_density()

### Graph
a: x: Float
a: y: Float
m: initialisation()

# (P2C2)

Quand on créer une methode le premier parametre par convention est "self":
def say_hello(self, first_name):

# (P2C3)

Quand on mes un dictionaire en parametre on doit le mettre avec 2 etoiles:

1. def __init__(self, agent_attributes):
2. def __init__(self, **agent_attributes):

1. agent = Agent(agent_attibutes)
2. agent = Agent(**agent_attibutes)

# (P2C4)

Le commit "C" deverait etre:

"Creation de la classe Position"
