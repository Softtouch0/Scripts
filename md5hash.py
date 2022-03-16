import hashlib
import colorama
from colorama import Fore


def openFile(wordlist):
    try:
        file = open(wordlist, 'r')
        return file
    except:
        print("File not found")
        quit ()


hashPassword = input ("Enter MD5 hash value here: ")
wordlist = input("Enter the wordlist path: ")
file = openFile(wordlist)



for word in file:
    print(Fore.LIGHTYELLOW_EX + '[+] Trying: ' + word.strip('\n'))
    encodedWord = word.encode('utf-8')
    try:
        md5Hash = hashlib.md5(encodedWord.strip(b'\n')).hexdigest()
        if md5Hash == hashPassword:
            print (Fore.GREEN + '[+] Password Found ' + word)
            exit()
        else:
            pass
    except Exception as e:
        pass


print ('[-] Password not in the List ')
