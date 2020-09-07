# Zero-Width-Character-Encryption
A encryption tool for hiding information using zwsp-steg-py.
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
