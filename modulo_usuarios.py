usuarios_list = []  # BD


# ------ validaciones -------------------
def validar_sexo(sexo):
    if sexo in ["F", "M"]:
        return True
    else:
        print("Error son valido F o M")
        return False

def validar_password(password):
    # debe tener mínimo 8 caracteres
    if len(password.strip()) > 8:
        print("Error min 8 caracteres")
        return False
    
    # que tenga al menos 1 numero
    tiene_numero = False
    for letra in password:
        if letra.isnumeric():
            tiene_numero = True
            
    # que tenga al menos 1 letra
    tiene_letras = False
    for letra in password:
        if letra.isalpha():
            tiene_letras = True
    
    if " " in password:
        print("Error no puede tener espacio")
        return False
           
    return tiene_letras and tiene_numero

def imprimir_usuario(usuario):
    print(f"""
    ---------------------------------
    Nombre usuario: {usuario["nombre_usuario"]}      
    Sexo: {usuario["sexo"]}
    Password: {usuario["password"]}
          """)


# ------ transacciones -------------------
