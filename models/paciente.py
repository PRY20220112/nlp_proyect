class Paciente():

    """Docstring for Paciente. """
    dni = ""
    peso = ""
    temperatura = ""
    altura = ""
    nombre = ""
    sexo = ""
    presion_arterial = ""
    grupo_sanguineo = ""
    procedencia = ""
    estadoCivil = ""
    edad = ""
    datos_adicionales = ""
    diagnostico = list()

    def __init__(self):
        self.diagnostico.clear()
        pass
