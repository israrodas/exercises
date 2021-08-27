listaR = []
listaP = []
respuesta = []
parametros = ["*,b,*", "a,*,*", "*,*,c", "foo,bar,baz", "w,x,*,*", "*,x,y,z" ]
rutas = [ "w/x/y/z", "a/b/c", "foo/", "foo/bar/", "foo/bar/baz" ]
for i in parametros:
    listaPatrones = i.split(sep=',')
    listaP.append(listaPatrones)
for i in rutas:
    listaRutas = i.split(sep='/')
    listaR.append(listaRutas)

pertenece=False    
for r in listaR:
    posicionIngresa = -1
    coincidenciasA = 0
    posicionCoincideA=0
    tRuta = len(r)
    posP=0    
    for p in listaP:
        posRS=-1
        coincidencias = 0
        posicionCoincide = 0
        tParam = len(p)
        if (tParam == tRuta):
            for rs in r:
                posRS+=1
                if (rs == p[posRS] or p[posRS]=="*"):
                    if (rs == p[posRS]):
                        coincidencias+=1
                        posicionCoincide = posRS
                    pertenece = True
                else:
                    pertenece = False
                    break
            if (pertenece):
                if (coincidenciasA < coincidencias):
                    posicionIngresa = posP
                if (coincidenciasA == coincidencias):
                    if (posicionCoincide < posicionCoincideA):
                        posicionIngresa = posP
                coincidenciasA = coincidencias
                posicionCoincideA = posicionCoincide
                pertenece = False
        else:
            if (len(p)+1 == len(listaP) and posicionIngresa < 0):
                posicionIngresa = -1
        posP+=1
    if (posicionIngresa >= 0):
        respuesta.append(listaP[posicionIngresa])
    else:
        respuesta.append("No Match")
print(respuesta)
    
