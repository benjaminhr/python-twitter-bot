from twython import Twython, TwythonError
import time

APP_KEY = "zx9UyoOfI693D50KDKlzPKWyw"
APP_SECRET = "szRyDakpY6Ms40ovi61sCNCUIK1vWlI5zMe84YAcOLJZ3i4jMr"
OAUTH_TOKEN = "190738750-VXHAqJU7vHwMK1Uy1i20CkmvlhYkXPvobU1xteAR"
OAUTH_TOKEN_SECRET = "HOOgGxG5ylFsSoFlDReKOgsfPDG6fooCVkGeEmKPFqdPS"

twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

try:
	with open('liners.txt', 'r+') as tweetfile:
		buff = tweetfile.readlines()

	for line in buff[:]:
		line = line.strip(r'\n')
		if len(line)<=140 and len(line)>0:
			print ("Tweeting...")
			twitter.update_status(status=line)
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			time.sleep(900)
		else:
			with open ('liners.txt', 'w') as tweetfile:
				buff.remove(line)
				tweetfile.writelines(buff)
			print ("Skipped line - Char length violation")
			continue
	print ("No more lines to tweet...")


except TwythonError as e:
	print (e)
