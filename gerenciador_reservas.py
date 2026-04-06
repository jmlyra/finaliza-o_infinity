import pandas as pd
from classes import Hotel, Cliente, Quarto, Reserva

class GerenciadorReservas:
    def __init__(self):
        self.reservas = []

    def criar_reserva(self, dono, quarto, data_checkin, data_checkout, status):
        # Verificar se o quarto está disponível nas datas
        for reserva in self.reservas:
            if (reserva.quarto == quarto and 
                not (data_checkout <= reserva.data_checkin or data_checkin >= reserva.data_checkout)):
                print(f"Quarto {quarto.numero} já está ocupado nas datas selecionadas.")
                return

        # Criar a reserva
        nova_reserva = Reserva(dono, quarto, data_checkin, data_checkout, status)
        self.reservas.append(nova_reserva)

        #  salvar no CSV
        dados = {
            "Cliente_nome":dono.nome,
            "cliente_id": dono.ID,
            "telefone": dono.tel,
            "email": dono.email,
            "quarto": quarto.numero,
            "tipo": quarto.tipo,
            "preco": quarto.preço,
            "checkin": str(data_checkin),
            "checkout": str(data_checkout),
            "status": status
        }

        try:
            df_existente = pd.read_csv("reservas.csv")
            df_novo = pd.DataFrame([dados])
            df_final = pd.concat([df_existente, df_novo], ignore_index=True)
        except FileNotFoundError:
            df_final = pd.DataFrame([dados])

        df_final.to_csv("reservas.csv", index=False)

        print("Reserva criada com sucesso!")
        
