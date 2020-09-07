'''
This is a beginner's work; sorry if the code is not that regulated.
A encryption tool for hiding information using zwsp_steg.
(pip install zwsp-steg-py) https://github.com/enodari/zwsp-steg-py
(Original coding: https://github.com/offdev/zwsp-steg-js)
You can disable the pyperclip by # related codes.
The "AA" in the default output is to make copy more easier.
You can place the string to your desired place and carefully delete the 2 "A"s.
(Just use pyperclip if you can install it.)
'''
import zwsp_steg
import pyperclip

def show_arrangement(data):
    if len(data) > 0:
        print ( data
            .replace ( '\u200b', '0' )
            .replace ( '\u200c', '1' )
            .replace ( '\u200d', '|' )
            .replace ( '\u200e', '>' )
            .replace ( '\u200f', '<' )
            )    
    else:
        print("No Valid Data!")
#This function is for demonstration only.

encoded = ""
decoded = "No decoded data." #default values

print("-----ENCODE INPUT-----") 
msg = input("Enter the secret message: ")
select_e = input("-----Select Mode----- \n1 = ZWSP \n2 = FULL : ")
if select_e == "1":
    encoded = zwsp_steg.encode(msg, zwsp_steg.MODE_ZWSP)
elif select_e == "2":
    encoded = zwsp_steg.encode(msg, zwsp_steg.MODE_FULL)
else:
    print("Invalid input")
    
try:
    if len(encoded) > 0:
        print("-----ENCODE OUTPUT-----")
        print("Example: "+"A"+ encoded + "A")
        print("Raw data copied to clipboard. The lenth of the raw string is "+str(len(encoded))+".")
        pyperclip.copy(encoded)  #Will copy the actual invisible data string only (No "A"s)
        show_arrangement(encoded)
        print("----------")    
    else:
        print("No encoded data.")    
except Exception as err:
    print("Error: "+str(err))
#encode part


print("-----DECODE INPUT-----") 
decode_msg = input("Enter the message with secret: ")
str0 = "\u200b" #verify string existence

if str0 in decode_msg:    #auto select mode
    try:
        decoded = zwsp_steg.decode(decode_msg, zwsp_steg.MODE_FULL)
    except Exception as err:
            print("Error: "+str(err)+" (FULL Mode)")
        
    try:
        decoded = zwsp_steg.decode(decode_msg, zwsp_steg.MODE_ZWSP)
    except Exception as err:
            print("Error: "+str(err)+" (ZWSP Mode)")
        
    try:
        print("-----DECODE OUTPUT-----")   
        print("Decoded Message: "+decoded)
        show_arrangement(decode_msg)
        print("-----END-----")   
    except Exception as err:
            print("Error: "+str(err))   
#if the data is corrupted, there will be 2 errors.
else:
    print("There's no secret message!")
    print("-----END-----")
#decode part