class Paciente():

    """Docstring for Paciente. """
    dni = " "
    peso = " "
    temperatura = " "
    altura = " "
    nombre = " "
    sexo = " "
    presion_arterial = " "
    grupo_sanguineo = " "
    procedencia = " "
    estado_civil = " "
    edad = " "
    datos_adicionales = " "
    diagnostico = list()
    antedecentes_personales = list()
    antedecentes_familiares = list()
    observaciones = list()

    def __init__(self):
        self.diagnostico.clear()
        self.antedecentes_personales.clear()
        self.antedecentes_familiares.clear()
        self.observaciones.clear()
        self.dni = " "
        self.peso = " "
        self.temperatura = " "
        self.altura = " "
        self.nombre = " "
        self.sexo = " "
        self.presion_arterial = " "
        self.grupo_sanguineo = " "
        self.procedencia = " "
        self.estado_civil = " "
        self.edad = " "
        pass
