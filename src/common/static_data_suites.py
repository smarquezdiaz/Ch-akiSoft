from enum import Enum

class StaticDataSuites(Enum):
    default_url_suite = ""
    default_url_suffix = "/DEMO"
    invalid_url_suffix_for_404 = "e"
    invalid_url_suffix = "/INVALID_PROJECT_CODE"

    valid_project_code_demo = "/DEMO"
    non_existent_project_code = "/TB"
    single_char_project_code = "/T"
    eleven_char_project_code = "/TTTTTTTTTTT"
    numeric_project_code = "/111"
    valid_limit_param = "/DEMO?limit=10"
    zero_limit_param = "/DEMO?limit=0"
    one_hundred_one_limit_param = "/DEMO?limit=101"
    string_limit_param = "/DEMO?limit=a"
    valid_offset_param = "/DEMO?offset=5"
    invalid_offset_param = "/DEMO?offset=100001"
    string_offset_param = "/DEMO?offset=a"