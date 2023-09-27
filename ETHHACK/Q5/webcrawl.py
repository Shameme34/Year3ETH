import requests

def check_subdirectories(url):
	try:
		r=requests.get(url)
		r.raise_for_status()
		print(url)
	except requests.exceptions.HTTPError as err: 
		pass


meta_ip = "10.0.2.5"
target_website = "http://"+meta_ip+"/mutillidae"

with open('dirs.txt','r') as f:
	for line in f:
		if(line == ""):
			pass
		else:
			directory = line.strip()		
			url = target_website + "/" + directory
			check_subdirectories(url)

