import hashlib
import secrets
import hmac

ITERATIONS = 600_000

def hash_function(password):

    salt = secrets.token_bytes(16)
 
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt,
        ITERATIONS
        )
    
    return salt.hex(), password_hash.hex()

def verify(typed_password ,salt ,password_hash):
    salt = bytes.fromhex(salt)
    new_hash = hashlib.pbkdf2_hmac(
            "sha256",
            typed_password.encode("utf-8"),
            salt,
            ITERATIONS
            )
    return hmac.compare_digest(new_hash.hex(),password_hash)
    

