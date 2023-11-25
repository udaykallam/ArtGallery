import pyotp

secret_key = pyotp.random_base32()
totp = pyotp.TOTP(secret_key)
otp = totp.now()
print("Generated OTP:", otp)
user_input = input("Enter the OTP: ")
is_valid = totp.verify(user_input)
if is_valid:
    print("OTP is valid!")
else:
    print("OTP is not valid!")
