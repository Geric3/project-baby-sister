# project-baby-sister
 Ce projet est concret et pratique pour le developpement d'application django web.
# Installation
  Pour installer ce projet, il faut d'abord s'assurer d'avoir la version 3 de python installer sur votre ordinateur. Crée un dossier pour votre projet et placez vous dans ce dossier. Créer un environnement virtuel pour votre projet avec venv:  
 `$ python3 -m venv env`  
Une fois l'environnement virtuel créé, il faut ensuite l'activer avec:  
`$ source env/bin/activate`  
installer les dépendances avec:  
`$ pip install -r requirements.txt`  
# Configuration
Rendez vous dans MySQL et créez votre base de donnée. 
Vous pouvez maintenant faire les migrations dans ta base de données avec:  
`$ python manage.py makemigrations`  
 `$ python manage.py migrate`  
Enfin démarrer votre projet avec la commande:  
`$ python manage.py runserver`  
