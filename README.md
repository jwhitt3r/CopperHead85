# Introduction
The CopperHead85 CTF challenge is focused at reverse engineering a compiled python exe that holds a BASE85(ASCII85) encoded password

# Compilation
To create the application the following applications are required: 

* Pyinstaller, 
* UPX, 
* Python 3.7+

## Python Script
The following is the contents of the Python script that was used to compare the input password with the Base85 flag.

```python
import argparse
import base64

parser = argparse.ArgumentParser(description='Welcome to the CopperHead85 USW CTF 2020 Challenge!', epilog='The UPX CyberChef is the best in packing!')
parser.add_argument('-p', action='store', type=str, dest="input_password", help="the password used to compare to answer", default=True)

zxcvf = "<DutG6Z6p_ATDHq@:WA:=#)Hb0LJf/I/"
args = parser.parse_args()

user_input = args.input_password
tmp_encode = base64.a85encode(user_input.encode('ascii'))
if tmp_encode.decode() == zxcvf:
  print("Congratulations you got the flag!")
else:
  print("This isn't the right flag!")
```

## Pyinstaller to EXE
Once the script is written, it is then passed into pyinstaller with the --onefile flag to ensure that all dlls are compiled with it.

```zsh
pyinstaller --onefile <script>.py
```

The final executable is then created into the 'dist' file.

## UPX Packing
Just for an added level of complexity to mess with any manual reverse engineering and a slight red-herring , the UPX tool is used.

```zsh
upx --best <script>.exe -o Copperhead.exe
```

# Clues


## Clue 1
The name of the file is a type of snake, this is a link between the programming language that the script is written in - Python.
In addition, the 85 is also a clue to the encoding type the flag is in - Base85 also referred to as ASCII85

```zsh
$ Copperhead85.exe -h
usage: Copperhead85.exe [-h] [-p INPUT_PASSWORD]
```

## Clue 2
Running the script.exe -h will output the clue: "The UPX CyberChef is the best in packing!"

```zsh
usage: Copperhead85.py [-h] [-p INPUT_PASSWORD]

Welcome to the CopperHead85 USW CTF 2020 Challenge!

optional arguments:
  -h, --help         show this help message and exit
  -p INPUT_PASSWORD  the password field used to compare to answer. Remember to
                     try quotes around the flag if the program/terminal
                     doesn't allow you to enter the flag e.g., 'Flag' or
                     "Flag"

The UPX CyberChef is the best in packing!
```

# Solving
The challenger is presented with a winx64 exe file that has been packed with UPX, and compiled with pyinstaller.

As it is an exe and compiled from python, we can use the pyinstaller unpacker from [Countercept](https://github.com/countercept/python-exe-unpacker)

```zsh
python pyinstxtractor.py Copperhead85.exe
```

From this output, we get a directory named Copper85.exe_extracted. In this file, the Copperhead85 file is provided (this is not a script but does provide the end answer).

Looking in the file, we next need to find a Base85 string

```
<DutG6Z6p_ATDHq@:WA:=#)Hb0LJf/I/
```

Taking this string we can either use python to decode from Base85 or we can use CyberChef as per the hint we can paste the Base85 string into the input, and add the "From Base85" to the Recipe. This should output the string
```
USW{CopperheadUSW2020CTF}
```
