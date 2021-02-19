MORSE_CODE = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z', '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9', '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!', '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':', '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_', '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'}
palabra = '.... . -.--   .--- ..- -.. .'

def decodeMorse(morse_code):
	lista = morse_code.replace("   ", " espacio ").split()
	result = ""
	
	for palabra in lista:
		if palabra == "espacio":
			result += " "
		else:
			result += MORSE_CODE[palabra]
	return result
	
	

x = MORSE_CODE.keys()
y = MORSE_CODE.values()
z = zip(y, x)
cmorse = dict()
for p1, p2 in z:
	cmorse[p1] = p2
	
	
def codeMorse(palabra):
	r = ""
	for p in palabra:
		r += cmorse[p] + " "
	return r
    
print(decodeMorse(palabra))
