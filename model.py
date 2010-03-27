from google.appengine.ext import db

class Ward(db.Model):
	name = db.StringProperty()	
	district = db.StringProperty()	
	county = db.StringProperty()	
	urban_arts_eclectic = db.FloatProperty()
	traditional_culture_vultures = db.FloatProperty()
	fun_fashion_and_friends = db.FloatProperty()
	mature_explorers = db.FloatProperty()
	dinner_and_a_show = db.FloatProperty()
	family_and_community_focused = db.FloatProperty()
	bedroom_djs = db.FloatProperty()
	mid_life_hobbyists = db.FloatProperty()
	retired_arts_and_crafts = db.FloatProperty()
	time_poor_dreamers = db.FloatProperty()
	a_quiet_pint_with_the_match = db.FloatProperty()
	older_and_home_bound = db.FloatProperty()
