import re
 
print(re.sub(r'\+?[78](\d{3})(\d{3})(\d\d)(\d\d)', r'+7(\1)\2-\3-\4', input()))
