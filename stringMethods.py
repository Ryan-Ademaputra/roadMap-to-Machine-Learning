# kamus lokal
tagline = 'Ryan is a Python programmer who loves to teach others about coding and software development.'

# convert tagline to uppercase    
print(tagline.upper()) ## upper

# convert tagline to lower
print(tagline.lower()) ## lower

# menghitung berapa banyak huruf
print(len(tagline)) ## len

print(tagline) ## normal

# mencari berapa banyak suatu karakter huruf
print(tagline.find('p'))
print(tagline.find('z'))
print(tagline.find('Python')) 

# menimpa suatu kalimat
print(tagline.replace('a Python programmer who loves to teach others about coding and software development.', 'kitten'))

# mencari suatu kalimat atau karaktek dengan mengembalikan nilai true or false
print('Rayner' in tagline)
print('Ryan' in tagline)