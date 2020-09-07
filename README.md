# Zero-Width-Character-Encryption
A encryption tool for hiding information using zwsp-steg-py.
This is a beginner's work; sorry if the code is not that regulated.
## Prerequisites:
* (pip install zwsp-steg-py) https://github.com/enodari/zwsp-steg-py
  * (Original coding: https://github.com/offdev/zwsp-steg-js)
* (pip install pyperclip) https://github.com/asweigart/pyperclip
```
An example of running the script:
[evaluate Zero-Width-Character-Encryption.py]
-----ENCODE INPUT-----
Enter the secret message: test
-----Select Mode----- 
1 = ZWSP 
2 = FULL : 1
-----ENCODE OUTPUT-----
Example: A​​​​​​‌‌​‍‍​​​​​​‌​‍​‍​​​​​​‌‌​‍‌​​​​​​‌‌​‍‍A
Raw data copied to clipboard. The lenth of the raw string is 44.
000000110||00000010|0|000000110|1000000110||
----------
-----DECODE INPUT-----
Enter the message with secret: A​​​​​​‌‌​‍‍​​​​​​‌​‍​‍​​​​​​‌‌​‍‌​​​​​​‌‌​‍‍A
Error: Unknown encoding detected! (FULL Mode)
-----DECODE OUTPUT-----
Decoded Message: test
A000000110||00000010|0|000000110|1000000110||A
-----END-----
```
