import crypt
import optparse
#Makes programs more dynamic by letting users specify password and dictionary files

#Function to obtain salt from hash and compare with hash from dictionary
def testPass(cryptPass, dname):
	salt = cryptPass[0:2]
	#salt is the first two characters of hash
	dictionaryFile = open(dname, 'r')
	for word in dictionaryFile.readlines()
		word = word.strip('\n')
		cryptWord = crypt.crypt(word, salt)
		#create encrypt dictionary word with salt
		if(cryptWord == cryptPass):
			print "[+] Found Password: " +word+ "\n"
			return
	print "[-] Password Not Found. \n"
	return

def Main():
	parser = optparse.OptionParser("usage %prog "+"-f <passwordFile> -d <dictionary>")
	parser.add_option('-f', dest='pname', type='string', help='specify password file')
	parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
	(options, args) = parser.parse_args()
	if(options.pname == None) | (options.dname == None):
		print parser.usage
		exit(0);
	else:
		pname = options.pname
		dname = options.dname

	passFile = open(pname, 'r')
	for line in passFile.readlines()
		if ":" in line:
			user = line.split(':')[0]
			#each new item split by colon
			cryptPass = line.split(':')[1].strip(' ')
			#strip any spaces
			print "[*] Cracling password for "+user+
			testPass(cryptPass, dname)

if __name__ == '__main__':
	Main():