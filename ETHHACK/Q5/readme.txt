1. Make sure Mutillidae is running properly
2. To run Mutillidae, type 
			sudo nano /var/www/mutillidae/config.inc
and change the $dbname to 'owasp10'
3. Once done, open kali and place the 'webcrawl.py' in the same directory as 'dirs.txt'.
4. run webcrawl.py with
			python3 webcrawl.py
5. Once up and running it will show all the websites that have matching subdirectories in the file.
