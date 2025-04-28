# ---- DÉBUT DU SCRIPT ----
import pandas as pd

# 1) Charger le jeu de données Iris
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
df = pd.read_csv(url)

# 2) Infos de base
print("Dimensions :", df.shape)
print("\nTypes de colonnes :\n", df.dtypes)
print("\nPremières lignes :\n", df.head())

# 3) Histogramme simple
import matplotlib.pyplot as plt

df['sepal_length'].hist()
plt.title("Distribution de sepal_length")
plt.xlabel("Longueur (cm)")
plt.ylabel("Fréquence")

# 4) Sauvegarde puis affichage
plt.savefig("histogramme.png")   # crée (ou écrase) le fichier PNG
plt.show()
