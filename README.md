# NSI1ere - ONLIFE
[![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]

Application du type "jeu de role" ou l'utilisateur se met dans la peau d'un personnage. (similairement a l'application "bitlife")
<br>Trello pour s'organiser: https://trello.com/b/nQkLOTQe


# Sommaire
**Information de base**
  - Membres
  - Partage des tâches
  - 16 Semaines
  - Description du jeu
  - Contrainte
  
**Professeur**
  - Etapes à suivre
  - Quelles sont les dificultés qui ont été surmontées ?
  - Quelles sont celles qu'il faut absolument régler au plus vite ?
  - Quelles sont celles qu'on aura pas le temps de surmonter et qu'est-ce que cela implique comme évolution sur le projet final ?
  - Rédiger 1 ou 2 paragraphes sur les principaux aspects techniques du projet (structure de données, modules de bibliothèque utilisés, interfaçage entre les différentes fonctions/fichiers, ...)
 


## Information de base

### Membres:
<br>Aurélie Gallet
<br>Clara Cuoghi
<br>Haroun Habidi
<br>Rayane Dahmoul


### Partage des tâches par élèves

Clara------ Aide pour rechercher comment coder les éléments et transmets les informations dans le readme.

Aurélie---- Page principal et les sous-parties, recherche d'informations pour les listes, écriture et relecture du readme.

Haroun----- Menu principal avec les différents boutons (Jouer, options, et quitter) et travail sur la conception visuelle global du jeu.

Rayane----- Menu de la deuxième page avec les boutons(Homme, Femme et retour) et mini-jeu (vaisseau qui tire sur des astéroides).


### 16 Semaines:
- 2 semaines de mise en place
- Coder les outils de base
- Ameliorer jusqu'a la semaine 13 ou 14
- Tester et rectifier 2-3 semaines



### Description du jeu

Nom du jeu: Onlife 

Un jeu ludique avec des fins qui diffèrent tout le temps. L'univers explore les différents fins du jeu ... Ce sera un jeu de rôle. On aura le choix de créer un personnage (sexe,nom,prénom). On contrôle les choix du personnage et le but est de devenir le plus riche possible (et d'accumuler tous les bagdes). Il y aura des choix qui nous permettront d'améliorer nos attitudes ou de les faire baisser. On pourra contrôler plusieurs générations. Pour avancer dans le jeu, on devra aller à l'école, acheter des biens ou les revendre, se marier... Il n'y a pas réellement de fin.



### Contrainte

Seulement avec du python

Seulement 16 semaines


## Professeur

### Etapes à suivre

Downloader toutes les images dans le folder images, tous les fichiers .py et ouvrir puis éxécuter le fichier "Onlife". Pour l'instant il y a un menu avec les boutons jouer et quitter qui marchent. 

Le bouton guide explique les règles principales du jeu et le bouton jouer nous emmène à un menu pour sélectionner le sexe. En fonction du sexe choisi, une page principale s'ouvrira avec un personnage aléatoire. Le nom est aussi aléatoire et en fonction du sexe. Il varie entre les noms des 4 personnes du groupe. Il est possible d'appuyer sur les boutons bien être, éducation et propriété qui vous ouvriront, chacun, une autre fenêtre. Il sera possible de fermer ces fenêtres avec le bouton pour vous ramener à la page principale. Il est également possible d'appuyer sur le bouton "+ une année" pour avancer dans le jeu ce qui va changer l'âge dans le cadre en haut à gauche de la page principale. 

La fenêtre éducation possède un titre qui change en fonction de l'âge, par exemple à 19 ans, le titre change d'enseignement" à "études supérieures". Des noms d'écoles sont affichés aléatoirement parmis les noms des dictionnaires. Puis en début d'université vous pouvez choisir votre spécialité. Vous aurez ainsi à 24 ans cinq choix de métiers en fonction de la spéciallité choisie. Puis vous pouvez jouer à un jeu de vaisseaux spatiaux afin de gagner plus d'argent.

La fenêtre propriété contient trois catégories d'objets, les domiciles, les transports et les animaux. Chaque catégorie contient un magasin dans lequel on peut acheter ce que l'on veut mais il y a un maximum de 7 articles.

La fenêtre bien-être n'est pas encore codée.



### Quelles sont les dificultés qui ont été surmontées ?

On a eu beaucoup de difficultés au début pour se mettre d'accord sur le jeu et la base du projet, on a pris quelques séances à se mettre d'accord . On avait tous un niveau assez bas en programmation et en plus de ça on ne connaissait pas du tout pygame. On a donc dû regarder de nombreux sites internet et des vidéos pour comprendre son fonctionnement et ses capacités. Une fois qu'on connaissait un peu les rudiments de la bibliothèque pygame on a eu quelques difficultés pour s'organiser, les garçons travaillaient beaucoup de leur côté à l'internat tandis que les filles essayaient de travailler ensemble pendant les cours. On n'était pas vraiment organisé par rapport à ce que faisait l'autre partie du groupe mais avec quelques séances d'entrainement on a réussi à travailler tous ensemble en s'aidant mutuellement. Pendant les séances en présentielles on arrivait plutôt bien à travailler mais pendant les séances à la maison c'était plus compliqué de s'organiser car il était plus compliqué de se montrer les codes qu'on programmait étant donné qu'on n'avait pas d'interaction physique, il fallait s'envoyer des photos de ce qu'on faisait où le mettre tout de suite sur github ce qui ralentissait légèrement l'avancée. Au niveau de la programmation on a eu un peu de mal pour coder l'ouverture d'une deuxième fenêtre, quand on trouvait un programme sur internet pour nous aider il était assez compliqué, donc on a dû le refaire de façon plus simple. 




### Quelles sont celles qu'il faut absolument régler au plus vite ?

Les difficultés qu'il nous faut régler assez vite sont tout d'abord de trouver un mini-jeu assez simple et supplémentaire qui nous permettra de rajouter de l'argent bonus dans notre jeu et pour le rendre plus ludique. La deuxième difficulté qu'il nous faut vite surmonter est de réussir à faire toutes les listes et les dictionnaires de chaque sous-pages. Nous avons aussi récemment decouvert un "beug" dans le jeu après avoir fait de nombreux test sans comprendre exactement pourquoi il survient. 

Mise à jour de la scéance du 16/02: Le mini-jeu est en cours de création, les listes sont faites pour la première page et il nous faut en faire pour la deuxième. Le beug est réglé.

Mise à jour de la scéance du 23/03: Les listes sont toutes crées. Un autre beug survient qu'on arrive pas a reproduire. Nous devons trouver un moyen de faire apparaitre des messages d'erreur.




### Quelles sont celles qu'on aura pas le temps de surmonter et qu'est-ce que cela implique comme évolution sur le projet final ?

La seule chose qui pour l'instant sera impossible de faire c'est des barres de vie qui devaient consister à afficher le niveau d'intelligence, taux de bonheur etc. du personnage tout le long de sa vie. Pour l'instant nous avons décidé de le mettre de côté ce qui ne changera pas le principe du jeu. Nous devons également renoncer à offrir tous les choix que nous aurions voulu offrir (le choix de l'école, arrêter l'école en avance ou sauter des classes par exemple).



### Rédiger 1 ou 2 paragraphes sur les principaux aspects techniques du projet (structure de données, modules de bibliothèque utilisés, interfaçage entre les différentes fonctions/fichiers, ...)

La plupart des spécifications pour le décor de la fenêtre se trouvent au début du code ainsi que des variables. L'extraction des images se fait au début et on a ensuite crée des listes (et bientôt des dictionnaires) nous même pour nous permettre de structurer et stocker les données comme le nom des établissements et des spécialités. 

Nous avons utilisé la bibliothèque pygame et pygame.locals car c'était plus simple pour nous en temps que débutants étant donné que c'est du python et c'est simple à comprendre et manipuler. Une autre bibliotèque que nous avons choisi est "pygame_menu" car nous voulions faire un menu et cette bibliotèque était pratique pour en créer. Puis nous avons importé le module "random" pour pouvoir déterminer aléatoirement les noms des écoles et probablement autres choses par la suite. Nous avons un système d'import entre plusieurs fichiers python pour le mini-jeu car c'est une solution simple que nous avons determiné pour relier nos deux travaux et pour avoir plus d'organisation dans le code.
Nous utilisons également temporairement la bibliothèque tkinter pour afficher des boites de dialogue afin de diriger le jouer pour qu'il sache quoi faire dans le jeu. Nous changerons vers une autre bibliothèque si nous trouvons un autre moyen d'afficher efficacement les boites de dialogue.

Nous avons des fonctions différentes reliées entre elles. Une d'elle définit le début du jeu (la fonction "depart"), donc la page d'accueil pour choisir entre jouer qui retourne la fonction "sexe", les options et donc la fonction "option_the_game" et quitter qui ferme la page. Elle se base sur pygame_menu est elle est reliée soit à la fonction "option_the_game" qui est vide pour le moment, soit celle de la page, aussi à base de pygame_menu, pour choisir son sexe (fonction "sexe") qui nous emmène ensuite à la fonction homme ou femme selon le choix. Les fonctions homme ou femme retourne ensuite l'éxécution de la fonction principale avec comme argument 1 ou 2. Cette fonction "principal"  prend en argument le sexe qui est codé par le numéro 1 ou 2 selon le sexe choisis. La fonction principale comporte des variables utilisées ensuite, plus de spécifications pour le décor de la fenêtre et de plusieurs boucles dans une grosse boucle. La grosse boucle fait tourner la page principale et les sous boucles font tourner les différentes sous pages comme l'éducation ou la propriété. Il y a aussi des boucles pour la détection d'événements surtout à base de clicks de la souris car notre jeu fonctionne surtout à partir des actions et de la position de la souris.


##  Licenses
This work is licensed under a



[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg
