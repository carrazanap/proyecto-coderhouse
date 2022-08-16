import pandas as pd

#Carga dateset
df_happiness2015 = pd.read_csv('./data/Happiness2015.csv')
df_happiness2016 = pd.read_csv('./data/Happiness2016.csv')
df_happiness2017 = pd.read_csv('./data/Happiness2017.csv')
df_happiness2018 = pd.read_csv('./data/Happiness2018.csv')
df_happiness2019 = pd.read_csv('./data/Happiness2019.csv')
df_happiness2020 = pd.read_csv('./data/Happiness2020.csv')
df_happiness2021 = pd.read_csv('./data/Happiness2021.csv')
df_happiness2022 = pd.read_csv('./data/Happiness2022.csv',decimal=",")

#Voy a agregar el año a todos los dataset y posteriormente unirlos
df_happiness2015['Year']=2015
df_happiness2016['Year']=2016
df_happiness2017['Year']=2017
df_happiness2018['Year']=2018
df_happiness2019['Year']=2019
df_happiness2020['Year']=2020
df_happiness2021['Year']=2021
df_happiness2022['Year']=2022

#Cambio nombre a las columnas ya que poseen diferentes nombres al pasar el año
df_happiness2015 = df_happiness2015.rename(columns={"Country":"Country","Happiness Rank":"Rank",
                                                    "Happiness Score":"Score","Economy (GDP per Capita)":"Economy",
                                                   "Family":"Family","Health (Life Expectancy)":"Health",
                                                   "Freedom":"Freedom","Trust (Government Corruption)":"Corruption",
                                                   "Generosity":"Generosity"})
#Dejo columnas que estan en todos los años
df_happiness2015 = df_happiness2015[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2016 = df_happiness2016.rename(columns={"Country":"Country","Happiness Rank":"Rank",
                                                    "Happiness Score":"Score","Economy (GDP per Capita)":"Economy",
                                                   "Family":"Family","Health (Life Expectancy)":"Health",
                                                   "Freedom":"Freedom","Trust (Government Corruption)":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2016 = df_happiness2016[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2017 = df_happiness2017.rename(columns={"Country":"Country","Happiness.Rank":"Rank",
                                                    "Happiness.Score":"Score","Economy..GDP.per.Capita.":"Economy",
                                                   "Family":"Family","Health..Life.Expectancy.":"Health",
                                                   "Freedom":"Freedom","Trust..Government.Corruption.":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2017 = df_happiness2017[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2018 = df_happiness2018.rename(columns={"Country or region":"Country","Overall rank":"Rank",
                                                    "Score":"Score","GDP per capita":"Economy",
                                                   "Social support":"Family","Healthy life expectancy":"Health",
                                                   "Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2018 = df_happiness2018[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2019 = df_happiness2019.rename(columns={"Country or region":"Country","Overall rank":"Rank",
                                                    "Score":"Score","GDP per capita":"Economy",
                                                   "Social support":"Family","Healthy life expectancy":"Health",
                                                   "Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2019 = df_happiness2019[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2020 = df_happiness2020.rename(columns={"Country name":"Country",
                                                    "Ladder score":"Score","Logged GDP per capita":"Economy",
                                                   "Social support":"Family","Healthy life expectancy":"Health",
                                                   "Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2020 = df_happiness2020[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2021 = df_happiness2021.rename(columns={"Country name":"Country",
                                                    "Ladder score":"Score","Logged GDP per capita":"Economy",
                                                   "Social support":"Family","Healthy life expectancy":"Health",
                                                   "Freedom to make life choices":"Freedom","Perceptions of corruption":"Corruption",
                                                   "Generosity":"Generosity"})
df_happiness2021 = df_happiness2021[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]
df_happiness2022 = df_happiness2022.rename(columns={"Country":"Country","RANK":"Rank",
                                                    "Happiness score":"Score","Explained by: GDP per capita":"Economy",
                                                   "Explained by: Social support":"Family","Explained by: Healthy life expectancy":"Health",
                                                   "Explained by: Freedom to make life choices":"Freedom","Explained by: Perceptions of corruption":"Corruption",
                                                   "Explained by: Generosity":"Generosity"})
df_happiness2022 = df_happiness2022[["Country","Score","Economy","Family","Health","Freedom","Corruption","Generosity","Year"]]

## Uno los dataframe
df_happiness = pd.concat([df_happiness2015, df_happiness2016, df_happiness2017, 
                          df_happiness2018,df_happiness2019,df_happiness2020,
                         df_happiness2021,df_happiness2022],ignore_index=True) 

#Exporto el dataframe final a .csv
df_happiness.to_csv('./data/Happiness_union.csv',index=False)

#Cantidad filas,cantidad columnas
print(f'Cantidad filas: {df_happiness.shape[0]} \nCantidad columnas: {df_happiness.shape[1]}')
