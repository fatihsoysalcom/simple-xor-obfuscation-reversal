import base64

def xor_encrypt_decrypt(data_bytes, key_bytes):
    """
    Encrypts or decrypts bytes using a repeating XOR key.
    This function is symmetric, meaning applying it twice with the same key
    will revert the data to its original state.
    """
    result = bytearray()
    key_len = len(key_bytes)
    for i, byte in enumerate(data_bytes):
        result.append(byte ^ key_bytes[i % key_len])
    return bytes(result)

# --- Simulating an application with obfuscated data ---

# 1. Original "secret" data that might be embedded in an application
original_secret_message = "Bu çok gizli bir yapılandırma mesajıdır." # This is a very secret configuration message.
print(f"Original secret message: {original_secret_message}\n")

# 2. A "key" used for obfuscation (often hardcoded or derived in real applications)
obfuscation_key = b"REA_KEY_123"

# 3. Obfuscation process:
#    Convert the original message to bytes, then XOR it with the key.
#    Finally, base64 encode the result to make it look like a compact, non-readable string
#    that might be found in a compiled binary or configuration file.
#    This is the "obfuscated" data a reverse engineer would encounter.
obfuscated_bytes = xor_encrypt_decrypt(original_secret_message.encode('utf-8'), obfuscation_key)
encoded_obfuscated_string = base64.b64encode(obfuscated_bytes).decode('ascii')

# This is what a reverse engineer might find in a binary or config:
print(f"Obfuscated and Base64 encoded string (as found in 'binary'):")
print(f"'{encoded_obfuscated_string}'\n")

# --- Simulating a reverse engineering process ---

# A reverse engineer would analyze the application's code/binary.
# They would identify the obfuscated string and try to find the de-obfuscation logic.
# Let's assume they found the obfuscated string and the key/algorithm.

# 1. Decode the base64 string back to its raw obfuscated bytes
found_obfuscated_bytes = base64.b64decode(encoded_obfuscated_string)

# 2. Apply the reverse (XOR) operation using the same key
#    (assuming the reverse engineer has identified the key and algorithm)
#    This step "reverses" the obfuscation.
deobfuscated_bytes = xor_encrypt_decrypt(found_obfuscated_bytes, obfuscation_key)

# 3. Decode the bytes back to a readable string
recovered_message = deobfuscated_bytes.decode('utf-8')

print(f"Recovered message after reverse engineering (de-obfuscation):")
print(f"'{recovered_message}'")

# Verification
assert recovered_message == original_secret_message
print("\nVerification successful: Recovered message matches original.")
