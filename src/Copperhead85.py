import argparse
import base64

parser = argparse.ArgumentParser(description='Welcome to the CopperHead85 USW CTF 2020 Challenge!', epilog='The UPX CyberChef is the best in packing!')
parser.add_argument('-p', action='store', type=str, dest="input_password", help="the password field used to compare to answer. Remember to try quotes around the flag if the program/terminal doesn't allow you to enter the flag e.g., 'Flag' or \"Flag\"", default=True)

zxcvf = "<DutG6Z6p_ATDHq@:WA:=#)Hb0LJf/I/"
args = parser.parse_args()

user_input = args.input_password
tmp_encode = base64.a85encode(user_input.encode('ascii'))
if tmp_encode.decode() == zxcvf:
  print("Congratulations you got the flag!")
else:
  print("This isn't the right flag!")
