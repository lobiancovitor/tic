import streamlit as st
import pandas as pd

data_gerais = pd.read_csv("dados_gerais.csv")
data_priv_pub = pd.read_csv("privadas_publicas.csv")  # Colocar % priv x pub
data_cursos = pd.read_csv("cursos.csv")
data_modalidade = pd.read_csv("modalidades.csv")
data_ranking = pd.read_csv("ranking.csv")

st.title("Ensino Superior - Sudeste")

st.write(
    "A região Sudeste é composta por quatro estados, sendo a mais populosa do Brasil."
)

st.write("Esse número se reverte no maior número de matrículas do país (43,8%).")

st.write("3.770.744 matrículas, sendo 25,8% no EAD")

#
#
#

st.subheader("Número de Matrículas por Estado")
st.bar_chart(data_gerais, x="Estado", y="Matrículas")

st.write("53,9% da matrículas totais da região estão no estado de São Paulo")


#
#
#

st.subheader("Matrículas em faculdades Privadas x Públicas por Estado")
st.bar_chart(
    data_priv_pub, x="Estado", y=["Publicas", "Privadas"], color=["#0000FF", "#FF0000"]
)

st.write("SP: 83,9% das matrículas totais são em instituições privadas. 76,3% são em cursos presenciais. Cursos mais procurados na rede privada: Direito e Administração.")

st.write("RJ: 73,8% das matrículas totais são em instituições privadas. 71,5% são em cursos presenciais. Cursos mais procurados na rede privada: Direito e Administração.")
#
#
#

estadoss = data_modalidade["Estado"].unique()
selecteds_estado = st.selectbox("Escolha um Estado", estadoss, key="estados_selectbox")

# Filtrar o DataFrame com base no estado selecionado
df_filtered = data_modalidade[data_modalidade["Estado"] == selecteds_estado]

# Pivotar o DataFrame para criar um gráfico de barras
df_pivot = df_filtered.pivot_table(
    index="Modalidade", columns="Rede", values="Matriculas", aggfunc="sum", fill_value=0
).reset_index()

# Ajustar o DataFrame para usar com st.bar_chart
df_pivot.set_index("Modalidade", inplace=True)

# Criar o gráfico de barras usando st.bar_chart()
st.write(f"### Matrículas por Modalidade e Rede - {selecteds_estado}")
st.bar_chart(df_pivot, use_container_width=True)

#
#
#

estados = data_cursos["Estado"].unique()
selected_estado = st.selectbox("Escolha um Estado", estados)
df_filtered = data_cursos[data_cursos["Estado"] == selected_estado]

# Pivotar o DataFrame para criar um gráfico de barras
df_pivot = df_filtered.pivot_table(
    index="Cursos",
    columns="Modalidade",
    values="Matriculas",
    aggfunc="sum",
    fill_value=0,
).reset_index()

# Ajustar o DataFrame para usar com st.bar_chart
df_pivot.set_index("Cursos", inplace=True)

# Criar o gráfico de barras usando st.bar_chart()
st.write(f"### Matrículas por Curso (rede privada) - {selected_estado}")
st.bar_chart(df_pivot, use_container_width=True)


#
#
#
st.write("### Ranking das Universidades")
st.markdown(
    data_ranking.to_html(classes="table table-striped", index=False),
    unsafe_allow_html=True,
)
st.markdown(
    """
    <style>
    .table {
        width: 100%;
        border-collapse: collapse;
    }
    .table th, .table td {
        padding: 15px;
        text-align: left;
        border-bottom: 1px solid #ddd;
    }
    .table tr:hover {
        background-color: #f5f5f5;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
