from enum import Enum

class StaticDataCustomField(Enum):
    valido_custom_post="/"
    valido_custom_field = "/5"
    vacio_custom_field = "/%20"
    negativo_custom_field = "/-1"
    decimal_positivo_custom_field = "/0.5"
    decimal_negativo_custom_field= "/-0.9"
    letras_custom_field = "/a"
    simbolo_custom_field = "/@"
    no_existe_custom_field = "/5000"
    sin_autenticar_custom_field = "/5"