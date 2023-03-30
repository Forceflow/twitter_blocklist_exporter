import json
import tweepy
import os
import datetime
import argparse

version="v0.1"

# Load API keys from json file
def load_keys():
	if os.path.exists("keys.json"):
		keysfile = open('keys.json', 'r')
		keys = json.load(keysfile)
		return keys
	else:
		print("No keys.json file found. Check the README on how to generate Twitter API tokens.")
		print("Check keys.json.example for an example keys.json file")
		print("Exiting.")
		quit()

# Output mutelist as HTML
def output_html_mutelist(mutelist):
	file = open("mutelist.html", "w")
	file.write("<html><head><title>My Twitter Mutelist</title></head><body>")
	now = datetime.datetime.now()
	file.write("<h1>Twitter mutelist generated on " + now.strftime("%Y-%m-%d %H:%M:%S") + "</h1>")
	file.write("<p>You have <strong>" + str(len(mutelist)) + "</strong> muted users.</p>")
	file.write("<p>The following list contains their last known username and numeric Twitter ID.</p>")

	file.write("<ul>")
	for muted_user in mutelist:
		line = "<li><a href=\"https://twitter.com/" + str(muted_user['screen_name']) + "\" target=\"_blank\">" + muted_user['screen_name']  + "</a> " \
		"(" + "<a href=\"https://twitter.com/i/user/" + str(muted_user['userid']) + "\" target=\"_blank\">" + str(muted_user['userid']) + "</a>)</li>"
		file.write(line)
	file.write("</ul></body></html>")

# Output blocklist as HTML
def output_html_blocklist(blocklist):
	file = open("blocklist.html", "w")
	file.write("<html><head><title>My Twitter Blocklist</title></head><body>")
	now = datetime.datetime.now()
	file.write("<h1>Twitter blocklist generated on " + now.strftime("%Y-%m-%d %H:%M:%S") + "</h1>")
	file.write("<p>You have <strong>" + str(len(blocklist)) + "</strong> blocked users.</p>")
	file.write("<p>The following list contains their last known username and numeric Twitter ID.</p>")

	file.write("<ul>")
	for blocked_user in blocklist:
		line = "<li><a href=\"https://twitter.com/" + str(blocked_user['screen_name']) + "\" target=\"_blank\">" + blocked_user['screen_name']  + "</a> " \
		"(" + "<a href=\"https://twitter.com/i/user/" + str(blocked_user['userid']) + "\" target=\"_blank\">" + str(blocked_user['userid']) + "</a>)</li>"
		file.write(line)
	file.write("</ul></body></html>")

# def read_blocklist_from_file(file):
# 	# Read blocklist
# 	inputfile = open('block.js', 'r')
# 	full_file = inputfile.read()
# 	# Find first occurence of "[" and strip to there
# 	full_file = full_file[full_file.index("["):]
# 	data = json.loads(full_file)
# 	blocklist = []
# 	# create a list of dictionaries, one dictionary per blocked user
# 	for item in data:
# 		blocklist.append({ 'userid' : item['blocking']['accountId'], 'userlink' : item['blocking']['userLink']})
# 	return blocklist

def get_blocklist_from_API(api):
	blocklist = []
	for user in tweepy.Cursor(api.get_blocks, skip_status=True).items():
		# We grab userid and screen_name
		blocklist.append({ 'userid' : user.id, 'screen_name' : user.screen_name})
	return blocklist

def get_mutelist_from_API(api):
	mutelist = []
	for user in tweepy.Cursor(api.get_mutes, skip_status=True).items():
		# We grab userid and screen_name
		mutelist.append({ 'userid' : user.id, 'screen_name' : user.screen_name})
	return mutelist

def main():
	print("Twitter Blocklist exporter " + version + " - https://github.com/Forceflow/twitter_blocklist_exporter")
	print("---")

	# Parse arguments
	parser = argparse.ArgumentParser(prog='Twitter Blocklist exporter')
	parser.add_argument('--mutelist', action='store_true')
	args = parser.parse_args()

	# Load settings from file
	print("Loading Twitter API keys from file")
	keys = load_keys()
	
	# blocklist = read_blocklist_from_file('block.js')

	# Do Twitter auth
	print("Authenticating with Twitter")
	auth = tweepy.OAuth1UserHandler(keys["API_KEY"], keys["API_KEY_SECRET"], keys["ACCESS_TOKEN"], keys["ACCESS_TOKEN_SECRET"])
	api = tweepy.API(auth)

	if args.mutelist is True:
		# Grab mutelist
		print("Grabbing mutelist")
		mutelist = get_mutelist_from_API(api)
		print(str(len(mutelist)) + " muted accounts found. Writing to mutelist.html")
		output_html_mutelist(mutelist)
	else:
		# Grab blocklist
		print("Grabbing blocklist")
		blocklist = get_blocklist_from_API(api)
		print(str(len(blocklist)) + " blocked accounts found. Writing to blocklist.html")
		output_html_blocklist(blocklist)

	
	print("Done. Exiting.")

if __name__ == "__main__":
	main()
