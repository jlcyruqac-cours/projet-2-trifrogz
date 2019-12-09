# 6_GEI505 PROJECT 2

## Équipe TriFrogz

Composée de Martin DELOR, Lauriane LEPAPE et Manon MICHELET

Conception d'un logiciel de softphone utilisant la téléphonie IP.

### Utilisation du logiciel de secours

- Cloner le repo GitHub du projet
> https://github.com/jlcyruqac-cours/projet-2-trifrogz

- Ouvrir le dossier "Partie 2_Solution_de_Secours"

- Exécuter le fichier MicroSIP-3.19.22.exe

- Télécharger FreeSWITCH

- Lancer en mode administrateur le fichier "FreeSwitchConsole.exe"

- Ouvrir MicroSIP et se connecter avec un identifiant se trouvant entre 1000 et 1015 et mettre 1234 comme mot de passe 

- Dans les paramètres de MicroSIP, dans "domaine", écrire votre adresse IP
> Ouvrir l'invite de commande, écrire "ipconfig", récupérer l'adresse se trouvant à "adresse IPv4"

- Votre logiciel est prêt à être utilisé.

### Utilisation de notre logiciel utilisant la console 

## Builder la librairie

- Récupérer le dossier .zip contenant le projet
> https://www.pjsip.org/download.htm

- Dans pj/include, créer une copie de "config_site_sample.h" à renommer par "config_site.h" puis supprimer l'original

- Ouvrir la solution du projet avec Visual Studio 2017

- Télecharger et installer la version 32 bits de Python 3.6.6

- Récupérer les fichiers "pjsua.c" et "pjsua.h" de ce repo GitHub :
> https://github.com/mgwilliams/python3-pjsip

- Les remplacer par ceux déjà présents dans le projet

- Supprimer le fichier _pjsua.def

- Clic droit sur la solution -> recibler la solution 

- Clic droit sur la solution -> Propriétés -> Répertoires VC++ -> Mettre les répertoires Include et Libs de python

- Clic droit sur python_pjsua -> définir comme projet de démarrage

- Compiler le logiciel en configuration Release sur la plateforme Win32

## Utilisation de la librairie Python

- Récupérer le fichier "communication.py" de notre repo GitHub

- Suivre les instructions écrites sur la console
