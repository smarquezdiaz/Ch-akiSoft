from enum import Enum

class StaticDataProject(Enum):
    valid_limit_param = "?limit=100&offset=0"
    invalid_url_param = "ss?limit=100&offset=0"
    invalid_limit1_param0 = "?limit=1&offset=0"
    invalid_limit0_param0 = "?limit=0&offset=0"
    invalid_limit_abc_param0 = "?limit=abc&offset=0"
    valid_limit5_param10 = "?limit=5&offset=10"
    invalid_limit10_param_1 = "?limit=10&offset=-1"
    invalid_limit101_param0 = "?limit=101&offset=0"
    invalid_limit_1_param0 = "?limit=-1&offset=0"
    invalid_limit5_param9999999 = "?limit=5&offset=9999999"

    valid_project_default = ""

    non_existent_project_code = "/suite/TB"
    single_char_project_code = "/suite/T"
    eleven_char_project_code = "/suite/TTTTTTTTTTT"
    numeric_project_code = "/suite/111"
    zero_limit_param = "/suite/DEMO?limit=0"
    one_hundred_one_limit_param = "/suite/DEMO?limit=101"
    string_limit_param = "/suite/DEMO?limit=a"
    valid_offset_param = "/suite/DEMO?offset=5"
    invalid_offset_param = "/suite/DEMO?offset=100001"
    string_offset_param = "/suite/DEMO?offset=a"