def checkPass(pass1: str, pass2: str):
    if len(pass1) >= 8 and pass1.isalnum() and pass1.lower() != pass1 and pass1 == pass2:
        return True
    return False


def checkUserParams(first_name, last_name, email, username, pass1, pass2):
    if username and first_name and last_name and email and "@" in email and "." in email and checkPass(pass1, pass2):
        return True
    return False
