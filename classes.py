class Hotel:
    def __init__(self):
        self.quartos = []
        self.reserva = []
        self.cliente = []


class Cliente:
    def __init__ (self,tel,email,ID,nome):
        self.tel = tel
        self.email = email
        self.ID = ID
        self.nome = nome


class Quarto: 
    def __init__ (self,numero,tipo,preço,status):
        self.numero = numero
        self.tipo = tipo
        self.preço = preço
        self.status = status

class Reserva:
    def __init__(self,dono,quarto,data_checkin,data_checkout,status):
        self.dono = dono
        self.quarto = quarto
        self.data_checkin = data_checkin
        self.data_checkout = data_checkout
        self.status = status