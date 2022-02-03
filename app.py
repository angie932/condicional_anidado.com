cantidad_bodega = int(input("Ingrese una cantidad en bodega: "));
cantidad_minima_requerida = int(input("Ingrese la cantidad minima requerida: "));


resta = cantidad_bodega - cantidad_minima_requerida;    
if (resta > 10):
    print ("Entonces no es necesario realizar el pedido al proveedor.");
    print ("Las unidades que faltan por vender son: " + str(resta));

if (cantidad_bodega <= cantidad_minima_requerida) :
    print ("Entonces si es necesario realizar el pedido al proveedor. ");
    cantidad_compra_deseada = int(input("Ingese la cantidad de compra deseada: "))
    valor_compra = int(input("Ingrese el valor de la compra: "));
    valor_caja = int(input("Valor de caja: "))
    print ("Cantidades de compra deseadas: " + str(cantidad_compra_deseada))
    print ("Valor de la compra: " + str(valor_compra));
    print ("Valor caja: " + str(valor_caja));
    if (valor_caja >= 1050000) :
        print("Si es posible realizar el pedido.");
    elif (valor_caja <= 400000) :
        print("No es posible realizar el pedido.");

elif (resta < 10 ) :
    print ("Entonces no es necesario realizar el pedido al proveedor.");
    print ("Unidades que hacen falta vender: " + str(resta));
    print ("¡ALERTA GENERADA!");

#POR TERMINAR
