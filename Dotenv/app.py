from dotenv import dotenv_values


conf = dotenv_values("secret.env")
values = conf.values()
access, secret = values

print(secret)