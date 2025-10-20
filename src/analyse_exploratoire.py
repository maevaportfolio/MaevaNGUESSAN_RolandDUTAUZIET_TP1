
##############################################################################################
# EXERCICE : Laissez libre court à votre créativité et créez une fonction qui affiche le taux
#            de valeurs manquantes de chaque variable pour chaque type (catégorielle et numérique)
#            par ordre décroissant
###############################################################################################         

def taux_missing_values(df):
    missing_values = df.isnull().mean()*100 # Calcul du pourcentage de valeurs manquantes par colonne
    missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
    if missing_values.empty:        
        print("Il n'y a pas de valeurs manquantes dans le dataset.")
    else:
        print("Taux de valeurs manquantes par variable :")
        for col, val in missing_values.items():
            print(f"{col:<10} : {val:.2f}%")   


#################################################################################################
# EXERCICE : Completer cette fonction qui retourne 0 ou 1 si la valeur observée est outlier ou pas 
##################################################################################################

def is_outlier(df,column):
    # 1er Quartile 
    Q1 = df[column].quantile(0.25)
    # 3ème Quartile 
    Q3 = df[column].quantile(0.75)
    # Inter-Quartile Range (IQR)
    IQR = Q3 - Q1
    # limites, basse & haute
    limite_inf = Q1 - 1.5 * IQR
    limte_sup = Q3 + 1.5 * IQR
    # Remplace les données inférieur et supérieur à la limite par 1 et les autres par 0
    series = df[column].apply(lambda x: 1 if (x < limite_inf or x > limte_sup) else 0)
    return series

##########################################################################################################
# EXERCICE : Laissez libre court à votre créativité et créez une fonction qui affiche le taux et nombre
#            de valeurs manquantes de chaque variable
#            par ordre décroissant
###########################################################################################################


def taux_missing_values_nb(df):
    missing_values = df.isnull().mean() * 100 # Calcul du pourcentage de valeurs manquantes par colonne
    missing_values_nb = df.isnull().sum() # Calcul du nombre de valeurs manquantes par colonne
    missing_values = missing_values[missing_values > 0].sort_values(ascending=False)
    if missing_values.empty:        
        print("Il n'y a pas de valeurs manquantes dans le dataset.")
    else:
        print("Taux de valeurs manquantes par variable :")
        for col, val in missing_values.items():
            print(f"{col:<10} : {val:.2f}%") 
        print("Nombre de valeurs manquantes par variable :")
        print(missing_values_nb[missing_values_nb > 0].sort_values(ascending=False))
