import hmac
import hashlib

def generate_hmac(key, message):
    """Generate an HMAC for a given message using the provided key."""
    return hmac.new(key.encode(), message.encode(), hashlib.sha256).hexdigest()

if __name__ == "__main__":
    key = "supersecretkey"
    message = "This is a secret message."
    
    # Generate HMAC
    hmac_hash = generate_hmac(key, message)
    print(f"Message: {message}")
    print(f"HMAC: {hmac_hash}")
