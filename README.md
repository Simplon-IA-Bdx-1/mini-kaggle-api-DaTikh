## Description

Créez une API à laquelle on peut envoyer des prédictions faites sur un dataset de test donné, via un "submission file" ayant les mêmes spécifications que sur Kaggle, et qui renvoie le score sur le dataset en question. 

On se basera sur le challenge GMSC. Vous pouvez créer cette API avec Flask, ou un autre outil de l'écosystème Python. Pour obtenir un dataset de test sur lequel les output sont connues, vous pouvez partager le dataset de train en 2. Enregistrez le dataset de test dans un fichier test2.csv, et fournissez un fichier contenant des prédictions sur ce dataset, qu'on nommera test2-predictions.csv.

Les commandes suivantes seront exécutées afin de tester votre travail:

```
pip install -r requirements.txt

export FLASK_APP=api.py
flask run

curl --request POST \
  --url 'http://localhost:5000/submit' \
  --header 'accept: multipart/form-data' \
  -F 'file=@test2-predictions.csv'
```

## Livrables

* requirements.txt contenant les dépendances Python
* api.py contenant le code de l'API
* split.py contenant le code qui partage le dataset de train en 2 et permet de créer test2.csv
* test2.csv
* predict.py contenant le code qui génère test2-predictions.csv
* test2-predictions.csv

Si possible, faites en sorte que les fichiers csv soient petits, afin que votre répo soit léger et rapidement téléchargeable (n'oubliez pas que vous êtes toute une promotion et qu'il faut télécharger tous vos repos pour les évaluer).

## Evaluation

* Présence et conformité des livrables
* Bon fonctionnement: je lance les commandes ci-dessus et j'obtiens bien un score d'AUC
* Code API correct: on récupère bien le csv envoyé dans la requête et on l'utilise dans le calcul de l'AUC
* Respect des best practices Python
* Présence et qualité des commentaires
* (Bonus) Présence de plusieurs commits et de commentaires de commit pertinents


## Mini-compétences visées

* Création d'un projet de code Python et push sur GitHub
* Installation et utilisation de librairies Python (par exemple flask)
* Gestion environnement Python (et spécifications d'environnement)
* Création d'un endpoint d'API basé sur une fonction Python:
  * code (api.py)
  * lancement du serveur (avec flask)
  * utilisation de l'API / test (avec curl)
* Chargement de données et utilisation dans une fonction de calcul de métrique de performance (AUC)