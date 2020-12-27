import pyshorteners

url = input("Please Enter your URL : ")
shortener = pyshorteners.Shortener()
a = shortener.tinyurl.short(url)
print(f'The Short URL is : {a}')

