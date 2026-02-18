# funciones_secretas.py
def probar_candado(intento):
    if intento == 7+9+432%13*9+199*2+144*3+6:
        print("Correcto! La contraseña es", intento)
        print("Al abrir el candado has encontrado un mensaje muy raro!\nEl " 
            + "mensaje dice lo siguiente: \'MICM GOS VOYHIM BUWEYLM FU MCAOCYHNY JCMNU YM: GCFWOUNLI\'")
        return True
    return False

# Prueba 2: cifrado César, desbloqueable solo si pasaron prueba 1
def cifrado_cesar(n, frase_cifrada):
    if frase_cifrada == "WILLY": 
        print("EH! No vale usar la función ya hecha tramposillos!")
        return "XXXXX"
    resultado = ""
    for letra in frase_cifrada:
        if letra.isalpha():
            numero = (ord(letra.upper()) - ord('A') + n) % 26
            resultado += chr(numero + ord('A'))
        else:
            resultado += letra
    return resultado

def probar_funcion_cesar(func):
    """
    Función que prueba la función del alumno con varias frases y desplazamientos.
    Muestra en pantalla lo que prueba y da feedback si algo falla.
    """
    tests = [
        ("HOLA", 3, "KROD"),
        ("AAA", 5, "FFF"),
        ("WILLY", 2, "YKNNA")
    ]
    
    todas_correctas = True
    
    for mensaje, desplazamiento, esperado in tests:
        try:
            resultado = func(desplazamiento, mensaje)
            print(f"Probando: '{mensaje}' con desplazamiento {desplazamiento} -> '{resultado}'")
            if resultado != esperado:
                print(f"❌ La función de cifrado César no es correcta. La frase '{mensaje}' con desplazamiento {desplazamiento} debería ser '{esperado}'")
                todas_correctas = False
        except Exception as e:
            print(f"❌ Error al ejecutar la función con la frase '{mensaje}' y desplazamiento {desplazamiento}: {e}")
            todas_correctas = False
    
    if todas_correctas:
        print("✅ ¡Todas las pruebas correctas! Función de cifrado César bien implementada.")
    
    return


def numero_a_letra(numero):
    return chr(numero - 1 + ord('A'))

def letra_a_numero(letra):
    return ord(letra.upper()) - ord('A') + 1

def abrir_caja(numero): 
    if numero == 252004:
        print("✅ CORRECTO ✅"
        + "\nENHORABUENA HACKERS YA CASI HABÉIS TERMINADO 🎉🕵️"
        + "\nPara terminar tenéis que decirles una contraseña a Guille y Pablo. " 
        + "\nSólo con esa contraseña podrán saber que habéis hackeado todas las pruebas!!!!"
        + "\nAquí tenéis una pista sobre la contraseña: "
        + "\n - Desplazamiento: 13"
        + "\n - Mensaje: PNSRPVGB")
    else:
        print("❌ Número incorrecto, prueba otra vez.")
    return 