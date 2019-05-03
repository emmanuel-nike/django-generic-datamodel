from cryptography.fernet import Fernet

def main(key, message):
    f = Fernet(key)
    print("called this")
    print(f.decrypt(message))


if __name__ == "__main__":
    key = 'TluxwB3fV_GWuLkR1_BzGs1Zk90TYAuhNMZP_0q4WyM='
    # Oh no! The code is going over the edge! What are you going to do?
    message = b'gAAAAABcwdAN-oDCRJTn9yP3mSb6QrBk9jq9x0tKgauDZKSO9-boPhjs6vExm2cmia5XNCDfvdIyonBpJAxUsn6Jv8m2uZm6T1F9FGsQ4BXvYdTCJQcmMIV4pt3QUsXRMVjA6YpjkfnfbHfLzbVIU44jBMnBp1J6ybVTmVg2R092-2Go3zC6Rsg='
    main(key, message)