from enum import Enum

class StaticDataPlans(Enum):
    default_url_suite = ""
    default_url_suffix = "/DEMO"
    invalid_url_suffix_for_404 = "e"
    invalid_url_suffix = "/INVALID_PROJECT_CODE"

    valid_project_code_demo = "/DEMO"
    lim_min_code = "/T"
    lim_max_code = "/TTTTTTTTTTTyrtyrtyrtrty"
    numeric_negative_code = "/-1236"
    char_special_code = "/#~@#€€"
    char_space = "/ "
    no_code = "/"

