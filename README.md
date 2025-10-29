# 📊 Analyse des ventes – SQLite & Pandas

Ce projet réalise une **analyse commerciale complète** à partir du dataset Kaggle *Sample Sales Data*.  
Il combine **SQLite** pour la structure de données et **Pandas** pour la manipulation et la visualisation.

---

## 🚀 Installation et exécution

### 1️⃣ Cloner le projet
```bash
git clone https://github.com/DonB31/...
cd ...
```


Creer et activer l'environnement virtuel

Mac/Linux
```bash
python -m venv sql_env
source sql_env/bin/activate
```

Sur Windows
```bash
python -m venv sql_env
.\sql_env\Scripts\activate
```
Installer les dependances

```bash
pip install -r requirements.txt
```
Selectionenr le kernel (Jupyter Notebook)

```bash
python -m ipykernel install --user --name=sql_env --display-name "Python (sql_env)"
```
.
├── data/
│   └── sales_data_sample.csv      # Dataset Kaggle
│    
│
├── notebook/
│   └── sql_requests.ipynb         # Analyses SQL et Pandas
│
├── src/
│   ├── download_dataset.py        # Télécharge le dataset
│   ├── create_tables_sqlite3.py   # Crée la table "ventes"
│   └── insert_values.py           # Insère les données
│
├── requirements.txt
├── database.db
└── README.md

Utilisation 
Telecharger le dataset

```bash
python src/download_dataset.py
```
Créer la table dans SQLite
```bash
python src/create_tables_sqlite3.py
```
Insérer les données
```bash
python src/insert_values.py
```

🧰 Outils utilisés

Python 3.12
SQLite3
Pandas
Matplotlib
KaggleHub
VS Code / Jupyter Notebook


📜 Licence

Projet personnel.
Données : Sample Sales Data © Kaggle — usage libre pour analyse non commerciale.