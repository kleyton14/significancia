
import scipy.stats as stats

# Dados de exemplo
grupo1 = [10, 12, 13, 15, 18]
grupo2 = [14, 16, 17, 19, 20]

# Teste t de Student
t_stat, p_valor = stats.ttest_ind(grupo1, grupo2)

# Resultados
print("t-estatística:", t_stat)
print("p-valor:", p_valor)

#O valor p é usado para determinar a significância. Um valor p menor que 0,05indica que há uma diferença significativa entre as duas amostras.