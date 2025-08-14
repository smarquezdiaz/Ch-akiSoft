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
    invalid_url_suffix_project = "/INVALID_PROJECT"


class StaticDataProjectPorCode(Enum):
    valid_code_param = "/DEMO"
    valid_code_param2 = "/EEEE"
    invalid_url_code= "ss/DEMO"
    invalid_no_exist_code = "/%DEmo"
    invalid_code_param = "/D"
    invalid_code_param_mas_limit = "/Dabcdefghijk"
    invalid_code_param_null = "   "
    invalid_code_param_special = "%$#^@"
    invalid_code_param_space = "/DE MO"
    invalid_code_param_number = "/12345"