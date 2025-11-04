# Projet de Pipeline CI/CD avec FastAPI

Ce projet est un exemple de mise en place d'une application Python FastAPI avec une pipeline d'intégration continue (CI) complète utilisant GitHub Actions.

## 🚀 Langage et Framework

* **Langage :** Python 3.10
* **Framework :** FastAPI

## ⚙️ Comment exécuter le projet manuellement

Suivez ces étapes pour exécuter l'application sur votre machine locale.

1.  **Clonez le dépôt (si ce n'est pas déjà fait) :**
    ```bash
    git clone [https://github.com/](https://github.com/)<VOTRE-NOM-UTILISATEUR>/<NOM-DU-DEPOT>.git
    cd <NOM-DU-DEPOT>
    ```

2.  **Créez un environnement virtuel (recommandé) :**
    ```bash
    python -m venv venv
    source venv/bin/activate  # Sur Windows: venv\Scripts\activate
    ```

3.  **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Démarrez le serveur de développement :**
    ```bash
    uvicorn main:app --reload
    ```
    * `--reload` permet au serveur de redémarrer automatiquement après chaque modification du code.

5.  **Accédez à l'application :**
    * Ouvrez votre navigateur à l'adresse [http://127.0.0.1:8000](http://127.0.0.1:8000)
    * Consultez la documentation interactive (Swagger UI) à [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

6.  **Exécutez les tests manuellement :**
    Pour lancer la suite de tests automatiques, exécutez simplement `pytest` dans votre terminal :
    ```bash
    pytest
    ```

## 🛠️ Étapes de la pipeline CI

La pipeline d'intégration continue est définie dans le fichier `.github/workflows/ci.yml` et s'exécute à chaque `push` ou `pull request` sur la branche `main`.

Voici les étapes qu'elle effectue :

1.  **Récupération du code** : La pipeline "check out" la version la plus récente de votre code.
2.  **Configuration de Python** : Elle installe un environnement Python propre (version 3.10).
3.  **Installation des dépendances** : Elle exécute `pip install -r requirements.txt` pour installer FastAPI, Pytest, etc.
4.  **Démarrage du serveur** : Elle lance le serveur `uvicorn` en arrière-plan.
5.  **Test de réactivité (curl)** : Elle attend 5 secondes, puis effectue un `curl` sur le point de terminaison racine (`http://localhost:8000/`) pour s'assurer que le serveur est démarré et répond correctement.
6.  **Exécution des tests automatiques** : Elle lance la commande `pytest` pour exécuter tous les tests (définis dans `test_main.py`) afin de valider la logique de l'application.

Si l'une de ces étapes échoue, la pipeline entière échoue, empêchant l'intégration de code défectueux.