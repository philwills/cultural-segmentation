from google.appengine.ext import db

import logging

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
	
	averages = {
		'urban_arts_eclectic': 4.5,
		'traditional_culture_vultures': 3.8,
		'fun_fashion_and_friends': 18.3,
		'mature_explorers': 10.5,
		'dinner_and_a_show': 19.8,
		'family_and_community_focused': 11.2,
		'bedroom_djs': 2.5,
		'mid_life_hobbyists': 4.3,
		'retired_arts_and_crafts': 2.8,
		'time_poor_dreamers': 6.7,
		'a_quiet_pint_with_the_match': 7.8,
		'older_and_home_bound': 5.5,
	}

	def nums(self):
		return {
			'urban_arts_eclectic': self.urban_arts_eclectic,
			'traditional_culture_vultures': self.traditional_culture_vultures,
			'fun_fashion_and_friends': self.fun_fashion_and_friends,
			'mature_explorers': self.mature_explorers,
			'dinner_and_a_show': self.dinner_and_a_show,
			'family_and_community_focused': self.family_and_community_focused,
			'bedroom_djs': self.bedroom_djs,
			'mid_life_hobbyists': self.mid_life_hobbyists,
			'retired_arts_and_crafts': self.retired_arts_and_crafts,
			'time_poor_dreamers': self.time_poor_dreamers,
			'a_quiet_pint_with_the_match': self.a_quiet_pint_with_the_match,
			'older_and_home_bound': self.older_and_home_bound,
		}
		
	def diff_from_average(self):
		return dict([[key, (self.nums()[key] - self.averages[key]) / self.averages[key]] for key in self.nums()])

	def biggest(self):
		biggest = ''
		biggest_value = 0

		logging.warn(biggest_value)
	
		for (name, difference) in self.diff_from_average().items():
			logging.warn(difference)
			if difference > biggest_value:
				biggest_value = difference
				biggest = name	
		return biggest.replace('_', ' ')
