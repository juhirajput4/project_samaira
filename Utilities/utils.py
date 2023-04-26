
import time
import string
import secrets

def getUniqueName(charCount=10):
    """
    Get a unique name
    """
    return getAlphaNumeric(charCount, "lower")

def getAlphaNumeric(length, type="letters"):
    """
    Get random string of characters
    Parameters:
        length: Length of string, number of characters string should have
        type: Type of characters string should have. Default is letters
        Provide lower/upper/digits for different types
    """
    alpha_num = ""
    if type == "lower":
        case = string.ascii_lowercase
    elif type == "upper":
        case = string.ascii_uppercase
    elif type == "digits":
        case = string.digits
    elif type == "mix":
        case = string.ascii_letters + string.digits
    else:
        case = string.ascii_letters
    return alpha_num.join(secrets.choice(case) for _ in range(length))