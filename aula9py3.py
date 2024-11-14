import streamlit as st
import pandas as pd
df=pd.DataFrame({'nome servidor': ['Adriana', 'Mônica', 'Samara'], 'salario':[10000,25000,20000]}
             )
st.write('Criando tabela')
st.write(df)
opcao = st.selectbox(
'Qual servidor você gostaria de selecionar?',
options=["Selecione..."] + df['nome servidor'].tolist()
)
