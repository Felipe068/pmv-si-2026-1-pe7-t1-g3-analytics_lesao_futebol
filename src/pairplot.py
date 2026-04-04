# Install dependencies as needed:
# pip install kagglehub[pandas-datasets]
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
  # Provide any additional arguments like 
  # sql_query or pandas_kwargs. See the 
  # documenation for more information:
  # https://github.com/Kaggle/kagglehub/blob/main/README.md#kaggledatasetadapterpandas
)

print("First 5 records:", df.head())

'''------------------------------------------------------------------'''

a = df.columns = df.columns.str.lower().str.strip().str.replace(" ", "_")
print(a)

#Gerando gráfico básico
sns.set_style("whitegrid")
plt.figure()
plt.hist(df["days"], bins=50)
plt.title("Distribuição da duração das lesões")
plt.xlabel("Dias lesionado")
plt.ylabel("Frequência")
plt.show()
