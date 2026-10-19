import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

df = pd.read_csv('orcamento.csv')

if 'orcamento' not in st.session_state:
    st.session_state['orcamento'] = df

st.title('Tabela de Preços')

servicos = df['Item / Serviço'].tolist()

col1, col2= st.columns(2)

with col1:
    item = st.selectbox('Item / Serviço', servicos)

with col2:
    quantidade = st.text_input('Quantidade')

if st.button('Adicionar'):
    st.session_state['orcamento'].loc[df['Item / Serviço'] == item,'Quantidade'] = int(quantidade)
    st.session_state['orcamento'].loc[df['Item / Serviço'] == item,'Subtotal'] = st.session_state['orcamento'].loc[df['Item / Serviço'] == item,'Preço Máximo (R$)'] * st.session_state['orcamento'].loc[df['Item / Serviço'] == item,'Quantidade']

st.dataframe(st.session_state['orcamento'])

st.markdown('---')
st.markdown(f"# Total: R${st.session_state['orcamento']['Subtotal'].sum()}")