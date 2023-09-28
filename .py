import pandas as pd
import matplotlib.pyplot as plt


arquivo = pd.read_csv('gasolina.csv', delimiter = ',')
plt.plot(arquivo['dia'], arquivo['venda'])
plt.xlabel('Dias')
plt.ylabel('Preço médio')
plt.title('Preço médio de vendas de Gasolina em julho/2021')
plt.savefig('line')