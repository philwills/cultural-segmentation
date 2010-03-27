import urllib
import urllib2
import csv

reader = csv.DictReader(open('Segments_and_area.csv'), fieldnames=['region', 'county', 'district', 'name', 'base', 'urban_arts_eclectic', 'traditional_culture_vultures', 'fun_fashion_and_friends', 'mature_explorers', 'dinner_and_a_show', 'family_and_community_focused', 'bedroom_djs', 'mid-life_hobbyists', 'retired_arts_and_crafts', 'time_poor_dreamers', 'a_quiet_pint_with_the_match', 'older_and_home_bound'])

url = 'http://cultural-segmentation.appspot.com/upload'

for line in reader:
    data = urllib.urlencode(line)
    req = urllib2.Request(url, data)
    urllib2.urlopen(req)

