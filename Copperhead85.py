import argparse
import base64

parser = argparse.ArgumentParser(description='Welcome to the CopperHead85 USW CTF 2020 Challenge!', epilog='The UPX CyberChef is the best in packing!')
parser.add_argument('-p', action='store', type=str, dest="input_password", help="the password used to compare to answer", default=True)

zxcvf = "6Z6p_ATDHq@:V>T<DusS0JY=L<(6"
args = parser.parse_args()

user_input = args.input_password
tmp_encode = base64.a85encode(user_input.encode('ascii'))
if tmp_encode.decode() == zxcvf:
  print("Congratulations you got the flag!")
else:
  print("This isn't the right flag!")
