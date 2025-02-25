
---

### **1. Importação de Bibliotecas**
```python
import pandas as pd
import seaborn as srn
import statistics as sts
```
- **`pandas`**: Biblioteca para manipulação e análise de dados.
- **`seaborn`**: Biblioteca para visualização de dados.
- **`statistics`**: Biblioteca para cálculos estatísticos.

---

### **2. Carregamento dos Dados**
```python
dataset = pd.read_csv("Churn.csv", sep=";")
dataset.head()
```
- **`pd.read_csv`**: Carrega um arquivo CSV em um DataFrame do Pandas.
- **`dataset.head()`**: Exibe as primeiras 5 linhas do DataFrame.

---

### **3. Verificação do Tamanho do Dataset**
```python
dataset.shape
```
- **`shape`**: Retorna o número de linhas e colunas do DataFrame.

---

### **4. Renomeação das Colunas**
```python
dataset.columns = ["Id", "Score", "Estado", "Genero", "Idade", "Patrimonio", "Saldo", "Produtos", "TemCartCredito", "Ativo", "Salario", "Saiu"]
```
- **`columns`**: Renomeia as colunas do DataFrame para nomes mais descritivos.

---

### **5. Exploração de Dados Categóricos**
```python
agrupado = dataset.groupby(['Estado']).size()
agrupado.plot.bar(color='gray')
```
- **`groupby`**: Agrupa os dados por uma coluna categórica.
- **`size`**: Conta o número de ocorrências em cada grupo.
- **`plot.bar`**: Cria um gráfico de barras para visualizar a distribuição.

---

### **6. Exploração de Dados Numéricos**
```python
dataset['Score'].describe()
srn.boxplot(dataset['Score']).set_title('Score')
srn.distplot(dataset['Score']).set_title('Score')
```
- **`describe`**: Gera estatísticas descritivas (média, desvio padrão, mínimo, máximo, etc.).
- **`srn.boxplot`**: Cria um boxplot para visualizar a distribuição e outliers.
- **`srn.distplot`**: Cria um histograma com uma curva de densidade.

---

### **7. Tratamento de Valores Ausentes (NAN)**
```python
dataset.isnull().sum()
dataset['Salario'].fillna(mediana, inplace=True)
```
- **`isnull().sum()`**: Conta o número de valores ausentes em cada coluna.
- **`fillna`**: Preenche valores ausentes com um valor específico (neste caso, a mediana).

---

### **8. Padronização de Dados Categóricos**
```python
dataset.loc[dataset['Genero'] == 'M', 'Genero'] = "Masculino"
dataset.loc[dataset['Genero'].isin(['Fem', 'F']), 'Genero'] = "Feminino"
```
- **`loc`**: Acessa um grupo de linhas e colunas para modificação.
- **`isin`**: Verifica se os valores estão em uma lista específica.

---

### **9. Tratamento de Idades Fora do Domínio**
```python
dataset.loc[(dataset['Idade'] < 0) | (dataset['Idade'] > 120), 'Idade'] = mediana
```
- Substitui idades inválidas (negativas ou maiores que 120) pela mediana.

---

### **10. Remoção de Dados Duplicados**
```python
dataset.drop_duplicates(subset="Id", keep='first', inplace=True)
```
- **`drop_duplicates`**: Remove linhas duplicadas com base em uma coluna (neste caso, `Id`).

---

### **11. Tratamento de Estados Fora do Domínio**
```python
dataset.loc[dataset['Estado'].isin(['RP', 'SP', 'TD']), 'Estado'] = "RS"
```
- Substitui estados inválidos por um valor padrão (neste caso, `RS`).

---

### **12. Tratamento de Outliers em Salário**
```python
desv = sts.stdev(dataset['Salario'])
dataset.loc[dataset['Salario'] >= 2 * desv, 'Salario'] = mediana
```
- **`sts.stdev`**: Calcula o desvio padrão.
- Substitui salários considerados outliers (maiores que 2 desvios padrão) pela mediana.

---

### **13. Verificação Final**
```python
dataset.head()
dataset.shape
```
- **`head`**: Exibe as primeiras linhas do DataFrame após as transformações.
- **`shape`**: Verifica o tamanho final do DataFrame.

---

### Resumo
O código realiza uma análise exploratória e tratamento de dados, incluindo:
1. Carregamento e visualização dos dados.
2. Renomeação de colunas.
3. Exploração de dados categóricos e numéricos.
4. Tratamento de valores ausentes, duplicados e fora do domínio.
5. Padronização de dados e remoção de outliers.
