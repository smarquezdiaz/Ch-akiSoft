from enum import Enum

class StaticDataSuites(Enum):
    default_url_suite = "/suite"
    default_url_suffix = "/suite/DEMO"
    invalid_url_suffix = "/suite/INVALID_PROJECT_CODE"

    valid_project_code_demo = "/suite/DEMO"
    non_existent_project_code = "/suite/TB"
    single_char_project_code = "/suite/T"
    eleven_char_project_code = "/suite/TTTTTTTTTTT"
    numeric_project_code = "/suite/111"
    valid_limit_param = "/suite/DEMO?limit=10"
    zero_limit_param = "/suite/DEMO?limit=0"
    one_hundred_one_limit_param = "/suite/DEMO?limit=101"
    string_limit_param = "/suite/DEMO?limit=a"
    valid_offset_param = "/suite/DEMO?offset=5"
    invalid_offset_param = "/suite/DEMO?offset=100001"
    string_offset_param = "/suite/DEMO?offset=a"