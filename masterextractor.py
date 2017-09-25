import io
import urllib2
import json
import time

def main(species_name):
	#species_name = species_name.replace(' ', '%20')
	url = "https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=%s&format=json&srlimit=1"%(species_name,)
	url = url.replace(' ', '%20')
	sphdr = {'User-Agent' : 'Mozilla/5.0'}
	reqobj = urllib2.Request(url, headers = sphdr)

	connection = False

	while connection is False:
		try:
			r = urllib2.urlopen(reqobj).read()
		except Exception as err:
			outfile = open("errors.log", "a")
			outfile.write(str(err))
			outfile.write(species_name+" si the species name\n")
			outfile.close()
			time.sleep(1)
		else:
			connection = True
	
	response_dict = json.loads(r)
	page_title = response_dict['query']['search'][0]['title']
	page_id = response_dict['query']['search'][0]['pageid']

	#page_title = page_title.replace(' ','%20')
	url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles=%s"%(page_title,)
	url = url.replace(' ', '%20')
	reqobj = urllib2.Request(url, headers = sphdr)

	connection = False

	while connection is False:
		try:
			r = urllib2.urlopen(reqobj).read()
		except Exception as err:
			outfile = open("errors.log", "a")
			outfile.write(str(err))
			outfile.write(species_name+" si the species name err2\n")
			outfile.close()
			time.sleep(1)
		else:
			connection = True

	response_dict = json.loads(r)
	extracted_text = response_dict['query']['pages'][str(page_id)]['extract']
	page_title = page_title.replace(' ','_')
	wikipedia_link = "https://en.wikipedia.org/wiki/"+page_title
	return extracted_text, wikipedia_link
#gives neat json response

# https://www.mediawiki.org/w/api.php?action=parse&summary=Some+%5B%5Blink%5D%5D&prop=