import pandas as pd
import streamlit as st
from gerenciador_reservas import GerenciadorReservas
from classes import Cliente, Quarto

# Inicializa o gerenciador
gerenciador = GerenciadorReservas()

# Título da aplicação
st.title("Sistema de Hospedagem")

# Formulário para inserir dados
st.header("Faça sua Reserva")


nome = st.text_input("Nome do Cliente")
telefone = st.text_input("Telefone do Cliente")
email = st.text_input("E-mail do Cliente")
cpf = st.text_input("CPF do cliente")

# Supondo uma lista de quartos
quartos = [
    Quarto(numero=101, tipo="Single", preço=150, status="Disponível"),
    Quarto(numero=102, tipo="Double", preço=250, status="Disponível"),
    Quarto(numero=103, tipo="Suite", preço=500, status="Ocupado"),
]

quarto_opcao = st.selectbox("Escolha o Quarto", options=[f"Quarto {q.numero} - {q.tipo} (R${q.preço})" for q in quartos])

data_checkin = st.date_input("Data de Check-in")
data_checkout = st.date_input("Data de Check-out")

status = st.selectbox("Status da Reserva", options=["Pendente", "Confirmada", "Cancelada"])

if st.button("Reservar"):
    # Encontra o quarto escolhido na lista
    quarto_escolhido = next(q for q in quartos if f"Quarto {q.numero} - {q.tipo} (R${q.preço})" == quarto_opcao)
    
    # Cria o cliente
    cliente = Cliente( tel=telefone, email=email, ID=cpf, nome = nome)  # ID pode ser gerado ou incrementado

    # Cria a reserva
    gerenciador.criar_reserva(
        dono=cliente,
        quarto=quarto_escolhido,
        data_checkin=data_checkin,
        data_checkout=data_checkout,
        status=status
    )
    st.success("Reserva criada com sucesso!")

#--------------------------atualizar----------------------------------------------

st.header("Atualizar Status da Reserva")

try:
    df = pd.read_csv("reservas.csv")

    if df.empty:
        st.warning("Nenhuma reserva encontrada.")
    else:
        # Mostrar tabela
        st.dataframe(df)

        # Criar identificador da reserva
        df["id_reserva"] = df.index

        # Escolher reserva
        reserva_id = st.selectbox(
            "Escolha a reserva para atualizar",
            options=df["id_reserva"]
        )

        # Escolher novo status
        novo_status = st.selectbox(
            "Novo Status",
            ["Pendente", "Confirmada", "Cancelada"]
        )

        if st.button("Atualizar Status"):
            df.loc[df["id_reserva"] == reserva_id, "status"] = novo_status

            # Remover coluna auxiliar
            df = df.drop(columns=["id_reserva"])

            # Salvar de volta no CSV
            df.to_csv("reservas.csv", index=False)

            st.success("Status atualizado com sucesso!")

except FileNotFoundError:
    st.error("Arquivo reservas.csv não encontrado.")


#------------------------------remover----------------------------------------------------------

    st.header("Cancelar / Apagar Reserva")

try:
    df = pd.read_csv("reservas.csv")

    if df.empty:
        st.warning("Nenhuma reserva encontrada.")
    else:
        # Criar ID temporário
        df["id_reserva"] = df.index

        # Mostrar tabela
        st.dataframe(df)

        # Selecionar reserva
        reserva_id = st.selectbox(
            "Escolha a reserva para apagar",
            options=df["id_reserva"]
        )

        if st.button("Apagar Reserva"):
            # Remover a linha
            df = df[df["id_reserva"] != reserva_id]

            # Remover coluna auxiliar
            df = df.drop(columns=["id_reserva"])

            # Salvar novamente
            df.to_csv("reservas.csv", index=False)

            st.success("Reserva apagada com sucesso!")

except FileNotFoundError:
    st.error("Arquivo reservas.csv não encontrado.")