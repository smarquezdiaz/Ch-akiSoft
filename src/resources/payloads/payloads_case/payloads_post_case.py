import uuid

def assert_request_payload(title: str, severity: int | None = None, priority: int | None = None,
                           type_: int | None = None, status: int | None = None, automation: int | None = None,
                           no_existe: str | None = None) -> dict:
    payload = {"title": title}

    if severity is not None: payload["severity"] = severity
    if priority is not None: payload["priority"] = priority
    if type_ is not None: payload["type"] = type_
    if status is not None: payload["status"] = status
    if automation is not None: payload["automation"] = automation
    if no_existe is not None: payload["no_existe"] = no_existe
    return payload


def name_random_cases(prefix: str = "soy el caso de prueba") -> str:
    return f"{prefix}_{uuid.uuid4().hex[:8]}"