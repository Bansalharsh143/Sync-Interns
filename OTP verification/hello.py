import random
import time

def generate_otp():
  """Generates a random OTP."""
  otp = random.randint(100000, 999999)
  return otp

def send_otp(phone_number, otp):
  """Sends an OTP to the given phone number."""
  # TODO: Implement sending an OTP via SMS or email.
  print("OTP sent to phone number: {}. OTP: {}".format(phone_number, otp))

def verify_otp(phone_number, otp):
  """Verifies the given OTP."""
  if otp == generate_otp():
    print("OTP verified.")
    return True
  else:
    print("OTP verification failed.")
    return False

def main():
  phone_number = input("Enter your phone number: ")
  otp = generate_otp()
  send_otp(phone_number, otp)
  otp_entered = input("Enter the OTP you received: ")
  if verify_otp(phone_number, otp_entered):
    print("You have successfully verified your OTP.")
  else:
    print("The OTP you entered is incorrect. Please try again.")

if __name__ == "__main__":
  main()