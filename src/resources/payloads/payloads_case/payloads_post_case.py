import uuid
import random
from src.common.static_data_cases import StaticDataCases

def case_request_payload(title: str | None = None, severity: int | None = None, priority: int | None = None,
                         type_: int | None = None, status: int | None = None, automation: int | None = None,
                         no_existe: str | None = None) -> dict:
    payload = {}

    if title is not None: payload["title"] = title
    if severity is not None: payload["severity"] = severity
    if priority is not None: payload["priority"] = priority
    if type_ is not None: payload["type"] = type_
    if status is not None: payload["status"] = status
    if automation is not None: payload["automation"] = automation
    if no_existe is not None: payload["no_existe"] = no_existe
    return payload


def name_random_cases(prefix: str = "soy el caso de prueba") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"

def random_severity_case():
    return random.choice([StaticDataCases.severity_critical_value.value,StaticDataCases.severity_major_value.value,
                          StaticDataCases.severity_normal_value.value,StaticDataCases.severity_minor_value.value])

def random_priority_case():
    return random.choice([StaticDataCases.priority_high_value.value,StaticDataCases.priority_medium_value.value,
                          StaticDataCases.priority_low_value.value])

def random_type_case():
    return random.choice([StaticDataCases.type_smoke_value.value,StaticDataCases.type_regression_value.value,
                          StaticDataCases.type_functional_value.value])

def random_status_case():
    return random.choice([StaticDataCases.status_actual_value.value,StaticDataCases.status_draft_value.value,
                          StaticDataCases.status_deprecated_value.value])

def random_automation_case():
    return random.choice([StaticDataCases.automation_is_not_automated_value.value,StaticDataCases.automation_automated_to_be_automated_value.value])

def decimal_number(int_):
    return float(int_) + 0.2