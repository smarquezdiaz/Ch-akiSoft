from enum import Enum

class StaticDataCases(Enum):
    severity_parameter = "severity"
    severity_critical_value = 2
    severity_critical_call = "/DEMO?severity=critical"
    severity_major_value = 3
    severity_major_call = "/DEMO?severity=major"
    severity_normal_value = 4
    severity_normal_call = "/DEMO?severity=normal"
    severity_minor_value = 5
    severity_minor_call = "/DEMO?severity=minor"

    priority_parameter = "priority"
    priority_high_value = 1
    priority_high_call = "/DEMO?priority=high"
    priority_medium_value = 2
    priority_medium_call = "/DEMO?priority=medium"
    priority_low_value = 3
    priority_low_call = "/DEMO?priority=low"

    type_parameter = "type"
    type_smoke_value = 2
    type_smoke_call = "/DEMO?type=smoke"
    type_regression_value = 3
    type_regression_call = "/DEMO?type=regression"
    type_functional_value = 8
    type_functional_call = "/DEMO?type=functional"

    status_parameter = "status"
    status_actual_value = 0
    status_actual_call = "/DEMO?status=actual"
    status_draft_value = 1
    status_draft_call = "/DEMO?status=draft"
    status_deprecated_value = 2
    status_deprecated_call = "/DEMO?status=deprecated"

    automation_parameter = "automation"
    automation_is_not_automated_value = 0
    automation_is_not_automated_call = "/DEMO?automation=is-not-automated"
    automation_automated_to_be_automated_value = 2
    automation_automated_to_be_automated_call = "/DEMO?automation=automated"

    title_one = "/a"
    title_lange = "/n sistemas operativos y aplicaciones, un nombre con más de 255 caracteres generalmente se considera un nombre largo, y puede causar problemas de compatibilidad o errores. La longitud máxima de 255 caracteres es común en sistemas de archivos y bases de datos, y se debe a restricciones técnicas en cómo se almacenan las cadenas de caracteres. "
    empty_title = " "
    id_does_not_exist = 100000
    negative_id = -10
    project_does_not_exist = "/no_existe"
    type_string = "soy_letras"
    value_does_not_exist = 1000
    empty_id = "  "
    special_id = "*[¨]["