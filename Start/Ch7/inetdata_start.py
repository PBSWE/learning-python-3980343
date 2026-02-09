# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request

web = urllib.request.urlopen('http://github.com/pbswe')
print('Result code:', web.getcode())
data = web.read()
print(data)