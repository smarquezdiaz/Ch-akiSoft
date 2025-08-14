from enum import Enum

class StaticDataCustomField(Enum):
    delete_custom_field1=""
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
    patch_script_custom_field ="<script>alert(\"XSS\")</script>"
    patch_custom_field ="/4"
    patch_custom_field1 = "/5"
    patch_custom_field2 = "/6"
    patch_custom_field3 = "/7"
    patch_custom_field4 = "/8"
    patch_custom_field_sin_id =""
    patch_custom_field_negativo = "/-3"
    patch_custom_field_decimal_positivo = "/0.4"
    patch_custom_field_decimal_negativo = "/-0.7"
    patch_custom_field_letras = "/a"
    patch_custom_field_simbolo = "/@"
    patch_custom_field_no_existe = "/300"


