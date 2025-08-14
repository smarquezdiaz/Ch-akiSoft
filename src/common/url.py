
def get_url_parametrized(get_url, module, params = None):
    return f"{get_url}/{module}{params}"

def assert_patch_join(modulo,id):
    return f"{modulo}/{id}"