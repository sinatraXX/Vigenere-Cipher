import detectEnglish

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def main():
	ciphertext = "Fqtkxèzr isxukb  qf g wmgnyl bl ovpxixgoxo nrzpnhobvi dmkz lg hysvt g cmeooa bl svgkbebbov Pgoanx mqcnozf, hkarj yv gno trzdmey yn n qogjubl. Vz oucrygf g pwes yn cuvgnrzpnhobvi ccoydqgadqbt."
	hackedMessage = hackVigenereDictionary(ciphertext)

	if hackedMessage != None:
		print(hackedMessage)
	else:
		print('Failed to hack encryption.')

def decryptMessage(key, ciphertext):
	translated = []
	keyIndex = 0
	key = key.upper()

	for letters in ciphertext:
		num = SYMBOLS.find(letters.upper())
		if num != -1:
			num -= SYMBOLS.find(key[keyIndex])
			num %= len(SYMBOLS)

			if letters.isupper():
				translated.append(SYMBOLS[num])
			elif letters.islower():
				translated.append(SYMBOLS[num].lower())
			
			keyIndex +=1
			if keyIndex == len(key):
				keyIndex = 0
		else:
			translated.append(letters)
	return ''.join(translated)

def hackVigenereDictionary(ciphertext):
	fo = open('dictionary.txt')
	words = fo.readlines()
	fo.close 

	for word in words:
		word = word.strip()
		decryptedText = decryptMessage(word, ciphertext)
		if detectEnglish.isEnglish(decryptedText, wordPercentage=40):
			print()
			print('Possible encryption break:')
			print('Key ' + str(word) + ':' + decryptedText[:300])
			print()
			print('Enter D for done, or just press Enter to continue breaking:')
			response = input('> ')

			if response.upper().startswith('D'):
				return decryptedText

if __name__ == '__main__':
	main()
