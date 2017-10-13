Hello, 

this is a cipher scipt written in Python 3.6. It is excuted from the command line and takes arguments when executed. Each file must have the .encode or .decode file extension to operate correctly. 

Example:
./vigenere -e (or -d) input.<encode or decode> output.<encode or decode> <Keyphrase>

----

./vigenere = File with scripts

-e or -d = encode or decode options

input = the input file. Make sure you use .encode or .decode file extensions to operate.

output = the output file, which will output to the location of the input file

keyphrase = the keyphrase used to encode or decode a message. if decoding make sure you use the same encode keyphrase to ensure proper decoding. 
