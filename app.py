tick = 1
ttask = 4
umax = 2
numUsuarios = 1
total = 0


listServer = []
Server = {
        "usuarios": 0,
        "inicio": 0,
        "fim": 0
    }

while(True) :
    numUsuarios = int(input('Digite a quantidade de usuários: '))
    if(numUsuarios > 0):
        inicioTick = tick
        fimTick = inicioTick + ttask
        if(len(listServer) == 0):
            while(numUsuarios > 0) :
                if(numUsuarios >= umax) :
                    usuarioDisponivel = umax
                    numUsuarios -= umax
                elif(numUsuarios > 0) :
                    usuarioDisponivel = numUsuarios
                    numUsuarios = 0

                server = {
                    "usuarios": usuarioDisponivel,
                    "inicio": inicioTick,
                    "fim": fimTick,
                }

                listServer.append(server)
        else :
            for x in listServer:
                if(x["usuarios"] < umax):
                    aux = umax - x["usuarios"]
                    if(aux >= numUsuarios):
                        x["usuarios"] += numUsuarios
                        x["fim"] = fimTick
                        numUsuarios = 0
                    else:
                        x["usuarios"] += aux
                        x["fim"] = fimTick
                        numUsuarios -= aux
            if(numUsuarios > 0):
                while(numUsuarios > 0) :
                    if(numUsuarios >= umax) :
                        usuarioDisponivel = umax
                        numUsuarios -= umax
                    elif(numUsuarios > 0) :
                        usuarioDisponivel = numUsuarios
                        numUsuarios = 0

                    server = {
                        "usuarios": usuarioDisponivel,
                        "inicio": inicioTick,
                        "fim": fimTick,
                    }

                    listServer.append(server)
    tick += 1

    if(tick == fimTick):
        break
print("custo total:\n")
for x in range(len(listServer)):
    total += 1 * (listServer[x]["fim"] - listServer[x]["inicio"])
    print("R$ 1 * ", (listServer[x]["fim"] - listServer[x]["inicio"]), " ticks (VM",x+1,")")
print("Total: ",total)
                    



