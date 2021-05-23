# Maria Isabel Ortiz Naranjo
# Proyecto 2 - Analisis de algoritmos 
# Carne: 18176

def mtf(configuracion, sol):
  sum = 0
  for i in sol:
    indice = configuracion.index(i) 
    configuracion.pop(indice)
    configuracion.insert(0, i)
    cost = indice + 1
    sum = sum + cost
    print("Lo que se solicitó: " + str(i))
    print("Costo:" + str(cost))
    print("configuracion: ",configuracion)
  print("El COSTO total: "+ str(sum))
  print("La configuracion FINAL: " ,configuracion)

def mtfch(config, request):
  i = 0
  cost = 0
  for value in request:
    i += 1
    if value in config:
      position = config.index(value)
      cost += position + 1
      if (position != 0):
        sub_req = request[(i):(i + position - 1)]
        if (value in sub_req):
          config.remove(value)
          config.insert(0, value)
    print("Solicitud: ", i, "Buscando: ", value, "Estado final configuración: ", config, "costo: ", cost)
    
# Solo quitar los comentarios para probar cada uno de los incisos

# Prueba inciso a
#x = [0, 1, 2, 3, 4]
#y = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
#mtf(x,y)

# Prueba inciso b
#x = [0, 1, 2, 3, 4]
#y = [4, 3, 2, 1, 0, 1, 2, 3, 4, 3, 2, 1, 0, 1, 2, 3, 4]
#mtf(x,y)

# Prueba inciso c
#y = []
#x = [0, 1, 2, 3, 4]
#for i in range(0,20):
  #b.append(0)
#mtf(x,y)

# Prueba inciso d
#y = [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0]
#x = [0, 1, 2, 3, 4]
#mtf(x,y)

# Prueba inciso e
#y = [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2]
#x = [0, 1, 2, 3, 4]
#mtf(x,y)

# Prueba inciso f
x = [0, 1, 2, 3, 4]
y = [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]
z = [0,1,2,3,4, 3,3,3,3,3, 1,1,1,1,1, 2,2,2,2,2, 4,4,4,4,4,4,4,]
#mtfch(x,y)

#worstcase = [4,3,2,1,0,4,3,2,1,0,4,3,2,1,0,4,3,2,1,0]
#mtfch(x, worstcase)
bestcase = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
mtfch(x, bestcase)

