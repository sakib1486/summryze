
def gen_sys_prompt(sys_prompt=""):
    if not sys_prompt:
        return f"You are a strict professional reviewer who strictly generates summary for a legal contract document with some specified parameters, and do not respond to any other queries."
    
    return sys_prompt