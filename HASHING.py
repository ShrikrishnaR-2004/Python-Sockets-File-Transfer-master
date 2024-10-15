"""Documentation
This module has two functions to encrypt and verify the hash

function     : encrypt()
Description  : Accepts a password string and returns hash if the following requirements are met otherwise,
               returns an empty string.
Requirements : Password must be longer than 8 characters.
               Must contain at least one uppercase letter.
               Must contain at least one lowercase letter.
               Must contain at least one special character.
               Must contain at least one number.

function     : verifier()
Description  : Returns a boolean value if the following requirements are met.
Requirements : Accepts a password string and hash, returns 1 on match otherwise, returns 0.
"""

import bcrypt
import string


def encrypt(password: str) -> str:
    try:
        if len(password) < 8 or len(password) > 73:
            raise ValueError
        number = string.digits
        white_space = string.whitespace
        lower_case = string.ascii_lowercase
        upper_case = string.ascii_uppercase
        special_char = string.punctuation

        NUM_FLAG, LOWER_FLAG, UPPER_FLAG, SPECIAL_CHAR_FLAG = False, False, False, False
        for i in password:
            if i in lower_case:
                LOWER_FLAG = True
                continue
            elif i in upper_case:
                UPPER_FLAG = True
                continue
            elif i in number:
                NUM_FLAG = True
                continue
            elif i in special_char:
                SPECIAL_CHAR_FLAG = True
                continue
            if i in white_space:
                raise AttributeError

        if not NUM_FLAG:
            raise Exception("Password must contain at least one number")
        elif not LOWER_FLAG:
            raise Exception("Password must contain at least one lowercase letter")
        elif not UPPER_FLAG:
            raise Exception("Password must contain at least one uppercase letter")
        elif not SPECIAL_CHAR_FLAG:
            raise Exception("Password must contain at least one special character")
        else:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return hashed_password.decode('utf-8')
    except ValueError:
        print ("Password must be at least 8 characters and at most 72 characters long")
        return ""
    except AttributeError:
        print("Password must must not contain white space characters")
        return ""

###############################################################################################################

def verifier(password: str, hash_string: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hash_string.encode('utf-8'))