class WeakPasswordError(Exception):
    pass

def login_counter(func):
    def wrapper(*args, **kwargs):
        print(f"Logging in for user: {args[0]}")
        try:
            func(*args, **kwargs)
        except WeakPasswordError as e:
            print(e)
    return wrapper

@login_counter
def login(username, password):
        if len(password) < 8:
            raise WeakPasswordError("Login failed: password too short\n")
        else:
            print("Login Successful\n")

login('john', '12345678')
login('joseph', '1234567')


