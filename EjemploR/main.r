coche <- function(color,aceleracion){

  output = list(
    ruedas = 4,
    color = color,
    aceleracion = aceleracion,
    velocidad = 0
  )
  class(output) <- "coche"
  return(output)
}

acelerar.coche <- function(x){
  x$velocidad = x$velocidad + x$aceleracion
}

frenar.coche <- function(x){
  v = x$velocidad - x$aceleracion
  if (v < 0){

  }
    v = 0.0
    x$velocidad = v
}

print("Ejemplo Programacion Orientada Objetos")

coche1 = coche(color="rojo", aceleracion=20)
cat("La velocidad del coche1 es", coche1$velocidad,"\n", sep="")
acelerar(coche1)
cat("La velocidad del coche1 es ", coche1$velocidad,"\n", sep="")
for (i in 1:10){
  acelerar(coche1)
}
cat("La velocidad del coche1 de color", coche1$color," es ", coche1$velocidad,"\n", sep="")

