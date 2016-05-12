#!/usr/bin/env python
import eztvit
import argparse
import sys

api = eztvit.EztvIt()

parser = argparse.ArgumentParser(description = "Get magnet links from eztv")
parser.add_argument('name', type=str, help='name of the show')

args = parser.parse_args()

all_shows = api.get_shows()

query = args.name.lower()

matched_shows = {show_id: show_name for show_id, show_name in all_shows.items() if query in show_name.lower()}

if len(matched_shows) == 0:
	print 'No matching shows found'
	sys.exit(0)
elif len(matched_shows) == 1:
	print 'Selecting ', matched_shows.items()[0]
	selected_show = matched_shows.items()[0][0]
else:
	print 'Found', len(matched_shows), 'matching shows:'
	shows = matched_shows.items()
	for show in shows:
		print show
	print 'Enter id of selected show:',
	selected_show = input()

all_episodes = api.get_episodes_by_id(selected_show)

seasons = all_episodes.keys()
print seasons
print 'Enter season number:',
season = input()

episodes = all_episodes[season].keys()
print episodes
print 'Enter episode number:',
episode = input()

links =  all_episodes[season][episode]

for link in links:
	print 'Release:', link['release']
	print 'Size (MB):', link['size_mb']
	print 'Magnet link:', link['download']['magnet']
	print ''
