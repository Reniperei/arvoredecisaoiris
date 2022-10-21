import streamlit as st

from sklearn.ensemble import RandomForestClassifier
import pandas as pd 

######################################################################
#                importando os dados do csv                          #

dados = pd.read_csv('/content/drive/MyDrive/IA claudio/Iris - Iris (1).csv')
######################################################################
#            separar as classes das features                         #
classes = dados['Species']
nomesColunas = dados.columns.to_list()
tamanho = len(nomesColunas)#quantos nomes tem
nomesColunas = nomesColunas[1:tamanho-1]
features = dados[nomesColunas]#monta o features

######################################################################
#            quebrar os dados em teste e treino                      #
from sklearn.model_selection import train_test_split

features_treino,features_teste,classes_treino,classes_teste = train_test_split(features,
                                                                               classes,
                                                                               test_size=0.4,
                                                                               random_state=2)

floresta = RandomForestClassifier(n_estimators=1000) 

floresta.fit(features_treino,classes_treino)

predicoes = floresta.predict(features_teste)
from sklearn import metrics


st.title('Repositorio IA')
nome = st.text_input('Digite o seu nome:')
if st.button('clique aqui'):
  st.write('bem vindo',nome,'ao seu primeiro aplicativo')
