import json
import os
from cryptography.fernet import Fernet

def load_or_create_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    return Fernet(key)

fernet = load_or_create_key()

def ensure_vault():
    if not os.path.exists('vault.json'):
        with open('vault.json', 'w') as vault_file:
            json.dump({}, vault_file)

def add_entry(site, username, password):
    ensure_vault()
    with open('vault.json', 'r') as vault_file:
        vault = json.load(vault_file)
    encrypted_password = fernet.encrypt(password.encode()).decode()
    if site not in vault:
        vault[site] = []
    vault[site].append({
        'username': username,
        'password': encrypted_password
    })
    with open('vault.json', 'w') as vault_file:
        json.dump(vault, vault_file, indent=2)
    print(f"Saved credentials for {site} (username: {username}).")

def view_entry():
    ensure_vault()
    with open('vault.json', 'r') as vault_file:
        vault = json.load(vault_file)

    if not vault:
        print("Empty vault")
        return
    print("Saved credentials:")
    for site, credentials in vault.items():
        print(f"/n {site}:")
        for account in credentials:
            decrypted_password = fernet.decrypt(account['password'].encode()).decode()
            print(f"   Username: {account['username']}")
            print(f"   Password: {decrypted_password}")