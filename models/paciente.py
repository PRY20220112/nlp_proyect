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
    antedecentes_personales = list()
    antedecentes_familiares = list()
    observaciones = list()

    def __init__(self):
        self.diagnostico.clear()
        self.antedecentes_personales.clear()
        self.antedecentes_familiares.clear()
        self.observaciones.clear()
        pass
