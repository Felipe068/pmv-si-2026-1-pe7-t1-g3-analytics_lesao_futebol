import kagglehub
from kagglehub import KaggleDatasetAdapter
import matplotlib.pyplot as plt
import seaborn as sns

# Set the path to the file you'd like to load
file_path = "full_dataset_thesis - 1.csv"

# Load the latest version
df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "sananmuzaffarov/european-football-injuries-2020-2025",
  file_path,
)

# Selecionar apenas colunas numéricas relevantes
df_pair = df[["player_age", "days", "games_missed"]]

# Gerar o pairplot
sns.pairplot(df_pair)
plt.show()
