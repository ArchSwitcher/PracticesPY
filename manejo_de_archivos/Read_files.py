import re #libreria de expresiones regulares

sample_file = open("sample", encoding="utf-8")
info = sample_file.read()

sample_file.close()

print(info)

print(re.search(r"\+\d-\(\d\d\d\)-\d\d\d-\d\d\d\d",info))


#\+\d-\(?\d{3}\)?-\(?\d{3}\)?-\(?\d\w{3}\)?