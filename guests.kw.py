name = input('what is your name?')
address = input(' what is your address?')
number = input('what is the phone number?')

with open('guest.txt', 'a') as file_object:
 	file_object.write('name')
 	file_object.write('address')
 	file_object.write('number')
 	
with open('guest.txt', 'a') as f:
	f = open('guest.txt')
print(f.name)
f.close()
print(f.closed)