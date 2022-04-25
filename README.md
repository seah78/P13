## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


### Déploiement

L'app est deployée en utilisant CircleCI, DockerHub et Heroku. 
Le pipeline est lancé à chaque push du repo sur la branche master et réalise les étapes suivantes :

- Construction et test
- Creation du conteneur Docker
- Déploiement sur Heroku 

Vous aurez besoin de déclarer les variables d'environnement soit dans un fichier .env pour lancer
l'application en local ou sur les plateformes de CircleCI ou Heroku pour un déploiement en ligne.

Liste des variables d'environnements pour CircleCI :
DEBUG
DOCKER_PASSWORD
DOCKER_USERNAME
HEROKU_APP_NAME
HEROKU_TOKEN
SECRET_KEY
SENTRY 

L'installation de Heroku en local est nécessaire pour le déploiement. (`https://devcenter.heroku.com/articles/getting-started-with-python#set-up`)

Utilisez la commande `heroku login` depuis un terminal afin de vous identifier sur votre compte Heroku 
Récupérez la variable d'environnement HEROKU_TOKEN, tapez la commande suivante : `heroku auth:token`


Vous devrez également changer la clé privée de votre DNS Sentry par la vôtre, ainsi que la fin de
l'adresse dans les settings du projet. Pensez également à changer le nom du domaine par celui de 
votre choix dans les ALLOWED_HOSTS des settings et dans la configuration du pipeline (config.yml),
lors de la dernière étape (heroku-deploy)


Lien du pipeline actuel:

https://app.circleci.com/pipelines/github/seah78/P13

Lien vers le site sur Heroku:

https://oc-lettings-site-seb.herokuapp.com/

Lien du Sentry (Vous devez avoir un compte Sentry et demander l'autorisation)

https://sentry.io/organizations/herlant/projects/oc-lettings-site-seb/?project=6358464&statsPeriod=14d