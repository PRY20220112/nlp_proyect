import spacy
from spacy.matcher import Matcher
from models.paciente import Paciente
from flask import jsonify

nlp = spacy.load("es_core_news_md")
matcher = Matcher(nlp.vocab)


def patrones():

    pattern = [{"TEXT": "presion"}, {"TEXT": "arterial"}, {"TEXT": "de"}, {"IS_DIGIT": True}]
    matcher.add("PRESION", [pattern])

    pattern = [
                [{"TEXT": {"REGEX": "[0-9]+[,.]?[0-9]+"}}, {"TEXT": "centimetros"}],
                [{"TEXT": {"REGEX": "[0-9]+"}}, {"TEXT": "centimetros"}]
             ]
    matcher.add("ALTURA", pattern)

    pattern = [{"TEXT": "temperatura"}, {"TEXT": "de"}, {"IS_DIGIT": True}, {"TEXT": "grados"}]
    matcher.add("TEMPERATURA", [pattern])

    pattern = [{"IS_DIGIT": True}, {"TEXT": "kilogramos"}]
    matcher.add("PESO", [pattern])

    pattern = [{"IS_DIGIT": True}, {"TEXT": "años"}]
    matcher.add("EDAD", [pattern])

    pattern = [{"TEXT": "DNI"}, {"IS_DIGIT": True}]
    matcher.add("DNI", [pattern])

    pattern = [
            [{"TEXT": "de"}, {"TEXT": "genero"}, {"TEXT": "femenino"}],
            [{"TEXT": "de"}, {"TEXT": "genero"}, {"TEXT": "masculino"}]
            ]
    matcher.add("SEXO", pattern)

    pattern = [
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "casado"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "casada"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "viudo"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "viuda"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "divorciado"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "divorciada"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "soltero"}],
                [{"TEXT": "estado"}, {"TEXT": "civil"}, {"TEXT": "de", "OP": "?"}, {"LOWER": "soltera"}],
            ]
    matcher.add("CIVIL", pattern)

# with open("./textos/datos6.txt", "r") as f:
#     text = f.read()


def procesar_texto(texto):
    patrones()
    text = texto
    doc = nlp(text)
    matches = matcher(doc)
    paciente = Paciente()
    # Matches
    for match_id, start, end in matches:

        string_id = nlp.vocab.strings[match_id]
        if string_id == "SEXO":
            matched_span = doc[end - 1:end]
            paciente.sexo = matched_span.text
            # print("Matcher:", string_id, ":", matched_span.text)
        elif string_id == "CIVIL":
            matched_span = doc[end - 1:end]
            paciente.estadoCivil = matched_span.text
            # print("Matcher:", string_id, ":", matched_span.text)
        elif string_id == "EDAD":
            matched_span = doc[start:end - 1]
            paciente.edad = matched_span.text
            # print("Matcher:", string_id, ":", matched_span.text)
        elif string_id == "DNI":
            matched_span = doc[end - 1:end]
            paciente.dni = matched_span.text
            # print("Matcher:", string_id, ":", matched_span.text)
        elif string_id == "PESO":
            matched_span = doc[start: end]
            paciente.peso = matched_span.text
        elif string_id == "TEMPERATURA":
            matched_span = doc[start + 2: end]
            paciente.temperatura = matched_span.text
        elif string_id == "ALTURA":
            matched_span = doc[start: end]
            paciente.altura = matched_span.text
        elif string_id == "PRESION":
            matched_span = doc[end - 1: end]
            paciente.presion_arterial = matched_span.text
        else:
            matched_span = doc[start:end]
            paciente.datos_adicionales += matched_span.text
            # print("Matcher:", string_id, ":", matched_span.text)

    for ent in doc.ents:
        if ent.label_ == "PER":
            if len(ent.text) > 6:
                paciente.nombre = ent.text
            # print("Estadistico", "Nombre: ", ent.text)
        if ent.label_ == "LOC":
            paciente.procedencia = ent.text
            pass
            # print("Estadistico", "Procedencia: ", ent.text)
    return jsonify(paciente.__dict__)
