# Bytemg
a simple text to image encoder

## How to use
To run the encoder:
```
python3 encode.py
```
Then, type in the text you want to encode. It will be output as `encoded.jpg`

To decode the image, run
```
python3 decode.py
```
in the console, it will print out the decoded data.

## How it works
It's a really simple Python script. 
To Encode the text, it takes the input, converts it into a byte array and then converts each individual byte value to binary.
After that, we convert those values to a string and draw them. 0 - white pixel , 1- black pixel. 
When decoding, it reads the image data pixel by pixel and stores the values, which it then converts into a string of binary and using
some stackoverflow and python magic converts them into chars which get joined into a string.
