	
def encryptor(text,number):
	number = number % 26

	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet_dict = {}
	reverse_alphabet_dict = {}
	
	i = 0
	for j in alphabet:
		alphabet_dict[j]=i
		reverse_alphabet_dict[i]=j
		i = i + 1
	
	encrypt=''
	for z in text:
		if z in alphabet_dict:
			a=0
			a=alphabet_dict[z]+number
			if a >25:
				a = a-26
			encrypt =encrypt +reverse_alphabet_dict[a]
		else:
			encrypt=encrypt+z
			
	return encrypt
	
def decryptor(text,number):
	number = number % 26
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	alphabet_dict = {}
	reverse_alphabet_dict = {}
	
	i = 0
	for j in alphabet:
		alphabet_dict[j]=i
		reverse_alphabet_dict[i]=j
		i = i + 1
	
	decrypt=''
	for z in text:
		if z in alphabet_dict:
			a=0
			a=alphabet_dict[z]-number
			if a < 0:
				a = a +26
			decrypt =decrypt +reverse_alphabet_dict[a]
		else:
			decrypt=decrypt+z
			
	return decrypt
	
a = encryptor('z',1)
b = decryptor(a,1)
print(a,b)
