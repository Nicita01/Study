# Vigener coder/decoder

this project allows to encode the text by the algorithm of the Fishener, to decode having a key or to decode without a key

## Vigener coder

If you want to encode your text on the Vigener cipher, place it on **text.txt**
Then, run **decoder.js**
Your open text (text, which you want to coding) should be in English, do not have any characters other than 26 English letters, including spaces between words, and also be in lowercase. If the text is not so, it will be brought to this form and placed in a file **simpleText.txt**
So, after run **decoder.js**, text from **text.js** will be brought into a normal form. All uppercase English letters will be converted to similar lowercase letters. And characters that are not part of the English alphabet will simply be ignored\
E: **text.txt:** *I love my life!!!*\
   **simpleText.txt:** *ilovemylife*\
Then, you must to enter your key, which will be use by cipher. And, then, coded text will be put to **codedText.txt**\
E: **simpleText.txt:** *ilovemylife*\
   **key:** *key*\
-> **codeText.txt:** *spmfikipgpi*

## Vigener decoder with key

If you have coded text in the desired form (see the first paragraph) and a key, you can decode it this way:\
Run **decoder.js**, then enter your key, which you know. Then, in terminal you will see decoding text. Also, decoding text will be puts on **decodeText.txt**.

## Vigener decrypt without a key

If you have encoded text, it must have the following properties so that it can be decoded:
- The text that was encoded should be meaningful, or at least a set of meaningful words. If a random set of letters was encoded, it is impossible to decode it
- The encoded text should be composed entirely of English letters in lower case, if it is not, you will get an exception
- The text should be large enough, and with increasing length of the key, the length of the text should also increase. On average, 72 is enough count of characters of meaningful plaintext for each key symbol

So, if your text meets the necessities mentioned above, place it on **codeText.txt**
Then, run **brakerMain.js** and, if it was posible, to decode your text, you will see decode text in terminal. Also, decoding text will be puts on **decodeText.txt**