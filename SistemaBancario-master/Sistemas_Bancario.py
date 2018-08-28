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
            self.id_userp = input("Digite la id de usuario: ")
            for iu in user:
                if iu['id'] == self.id_userp:
                    self.id_pres = input("Digite la id prestamo: ")
                    self.cant_pres = int(input("Ingrese la cantidad del prestamo: "))
                    self.num_cuo_pres = int(input("Ingrese numero de cuotas del prestamo: "))
                    pres.append({'id_user': self.id_userp, 'id_pres': self.id_pres, 'can_pres': self.cant_pres,
                                 'num_cuo': self.num_cuo_pres})
                    nc = self.num_cuo_pres
                    if (nc > 0):
                        c = 0
                        valor_cuota = self.cant_pres / self.num_cuo_pres
                        while c != nc:
                            cuo.append({'id_user': self.id_userp, 'id_pres': self.id_pres, 'num_cuo': c + 1,
                                        'valor_cuo': valor_cuota, 'estado': False})
                            c = c + 1

class Cuota:
    id_userpc = 0
    id_presc = 0
    id_u = 0
    def Mostar_Pagar_cuota(self):
        self.id_userpc = input("ingrese la id del usuario: ")
        self.id_presc = input("ingrese la id del prestamo: ")
        for iup in cuo:
            if iup['id_user'] == self.id_userpc and iup['id_pres'] == self.id_presc:
                print(iup['num_cuo'], iup['valor_cuo'])
        cp = int(input("Digite el numero de la cuota a pagar: "))
        for bc in cuo:
            if bc['id_user'] == self.id_userpc and bc['id_pres'] == self.id_presc:
                if bc['num_cuo'] == cp:
                    if bc['estado'] == False:
                        bc['estado'] = True

        #Reportes

    def Cuotas_pagadas(self):
        self.id_userpc = input("ingrese la id del usuario a consultar: ")
        self.id_presc = input("ingrese la id del prestamo a consultar: ")
        cpa = 0
        for c_pa in cuo:
            if c_pa['id_user'] == self.id_userpc and c_pa['id_pres'] == self.id_presc:
                if c_pa['estado'] == True:
                    cpa = cpa + 1
        print("Las cuotas pagadas son {} por valor de {}".format(cpa, c_pa['valor_cuo']))

    def Numero_Cuota_Mora(self):
        self.id_userpc = input("ingrese la id del usuario a consultar: ")
        self.id_presc = input("ingrese la id del prestamo a consultar: ")
        cm = 0
        for c_p_m in cuo:
            if c_p_m['id_user'] == self.id_userpc and c_p_m['id_pres'] == self.id_presc:
                if c_p_m['estado'] == False:
                    cm = cm+1
        print("Las cuotas en mora son {} por valor de {} ".format(cm, c_p_m['valor_cuo']))

    def Todos_Prestamo(self):
        self.id_u=input("Digite su identificacion: ")
        for tp in pres:
            if tp['id_user'] == self.id_u:
                print("La id del prestamo es {} por un valor de {} diferido a {} cuotas ".format(tp['id_pres'], tp['can_pres'], tp['num_cuo']))


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
opc =int(input("Digite la opcion del MENU PRINCIPAL: "))


while opc != 5:
    usuario = User()

    if opc == 1:
        usuario.Registro_User()
        #print(user)
        print("\n")

    elif opc == 2:
        if user:
            usuario.Registrar_prestamo()
            print("\n")
        else:
            print("no hay usuarios registrados")
    elif opc == 3:
        if pres:
            usuario.Mostar_Pagar_cuota()
            #print(cuo)
            print("\n")
        else:
            print("No hay prestamos realizados")
    elif opc == 4:
        if cuo:
            print("\n")
            print("MENU DE REPORTES")
            print("1. Consultar numero de cuotas pagadas")
            print("2. Consultar numero de cuotas en mora")
            print("3. Consultar todos sus prestamos")
            print("4. Regresar al MENU PRINCIPAL")
            print("\n")
            nopc = int(input("Digite la opcion del MENU DE REPORTES: "))
            while nopc != 4:

                if nopc == 1:
                    print("\n")
                    usuario.Cuotas_pagadas()
                    #print("1,1")
                    print("\n")
                elif nopc == 2:
                    print("\n")
                    usuario.Numero_Cuota_Mora()
                    #print("1,2")
                    print("\n")
                elif nopc == 3:
                    print("\n")
                    usuario.Todos_Prestamo()
                    #print("1,3")
                    print("\n")
                else:
                    print('La opcion digitada no existe')

                print("\n")
                nopc = int(input("Digite la opcion del MENU DE REPORTES: "))
        else:
            print("\n")
            print("No hay informacion registrada")
            print("\n")
    else:
        print('La opcion digitada no existe')

    opc =int(input("\nDigite la opcion del MENU PRINCIPAL: "))
