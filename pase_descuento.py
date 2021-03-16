edad=int(input("Digame su edad:"))
tipo_de_doc=input("Digame que documento tiene: E(Estudiante) - P(Pensionista) - F(Familia Vulnerable) - N(Nada):")

if (edad < 35 and edad >25 and tipo_de_doc == "E") or (edad > 65 and tipo_de_doc == "P") or (edad < 12) or (tipo_de_doc == "F" ):
    print("Se te aplica el descuento")