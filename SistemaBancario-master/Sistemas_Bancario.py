#ALejandra Salas

user = []
pres = []
cuo = []

class Prestamo:
    id_userp = 0
    id_pres = 0
    cant_pres = 0
    num_cuo_pres = 0

    def Registrar_prestamo(self):
        self.id_userp = input("digite la id de usuario: ")
        for iu in user:
            if iu['id'] == self.id_userp:
                self.id_pres = input("digite la id prestamo: ")
                self.cant_pres = int(input("Ingrese la cantidad del prestamo "))
                self.num_cuo_pres = int(input("Ingrese numero de cuotas del prestamo "))
                pres.append({'id_user': self.id_userp, 'id_pres': self.id_pres, 'can_pres': self.cant_pres, 'num_cuo': self.num_cuo_pres})
                nc = self.num_cuo_pres
                if (nc > 0):
                    c = 0
                    valor_cuota = self.cant_pres/self.num_cuo_pres
                    while c != nc:
                        cuo.append({'id_user': self.id_userp, 'id_pres': self.id_pres, 'num_cuo':c+1,'valor_cuo': valor_cuota, 'estado':False})
                        c = c + 1

class Cuota:
    id_userpc = 0
    id_presc = 0
    id_u = 0
    def Mostar_Pagar_cuota(self):
        self.id_userpc = input("ingrese la id del usuario: ")
        self.id_presc = input("ingrese la id del prestamo a pagar: ")
        for iup in cuo:
            if iup['id_user'] == self.id_userpc and iup['id_pres'] == self.id_presc:
                print(iup['num_cuo'], iup['valor_cuo'])
        cp = int(input("Digite el numero de la cuota a pagar: "))
        for bc in cuo:
            if bc['num_cuo'] == cp:
                if bc['estado'] == False:
                    bc['estado'] = True

        #Reportes

    def Cuotas_pagadas(self):
        for c_pa in cuo:
            if c_pa['estado'] == True:
                print("Las cuotas pagadas son:{} {}".format(c_pa['num_cuo'], c_pa['valor_cuo']))

    def Numero_Cuota_Mora(self):


        for c_p_m in cuo:
            if c_p_m['estado'] == False:
                cm = cm+1
                print("Las cuotas en mora son {} por valor de {} ".format(cm, c_p_m['valor_cuo']))

    def Todos_Prestamo(self):
        self.id_u=input("Digite su identificacion: ")
        for tp in pres:
            if tp['id_user'] == self.id_u:
                print("La id del prestamos es {} por un valor de {} diferido a {} cuotas ".format(tp['id_pres'], tp['can_pres'], tp['num_cuo']))


class User(Prestamo, Cuota):
    Id_user = 0
    nom_user = ""

    def Registro_User(self):
        self.Id_user = input("Ingrese su identificacion: ")
        self.nom_user = input("Digite su nombre: ")
        user.append({'id': self.Id_user, 'nom': self.nom_user})


print("MENU DE OPCIONES")
print("1. Crear Usuario")
print("2. Solicitar Prestamo")
print("3. Pagar cuotas")
print("4. Reportes")
print("\n")
opc =int(input("Digite la opcion: "))


while opc != 5:
    usuario = User()

    if opc == 1:
        usuario.Registro_User()
        print(user)

    elif opc == 2:
        usuario.Registrar_prestamo()
        print(pres)
        print(cuo)

    elif opc == 3:
        usuario.Mostar_Pagar_cuota()
        print(cuo)

    elif opc == 4:
        print("1. Consultar numero de cuotas pagadas")
        print("2. Consultar numero de cuotas en mora")
        print("3. Consultar todos sus prestamos")

        nopc = int(input("Digite la opcion para de reportes que desea optener: "))
        while nopc != 4:

            if nopc == 1:
                usuario.Cuotas_pagadas()
                print("1,1")

            elif nopc == 2:
                usuario.Numero_Cuota_Mora()
                print("1,2")

            elif nopc == 3:
                usuario.Todos_Prestamo()
                print("1,3")

            else:
                print('La opcion digitada no existe')

            nopc = int(input("\nDigite la opcion Nuevamente: "))

    else:
        print('La opcion digitada no existe')

    opc =int(input("\nDigite la opcion: "))
