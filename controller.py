import os

import csv

from model import Ward

import logging

from google.appengine.ext import webapp
from google.appengine.ext.webapp import template

class ModelAndViewPage(webapp.RequestHandler):
	def render(self, view, model={}):
		path = os.path.join(os.path.dirname(__file__), 'templates', view)
		self.response.out.write(template.render(path + '.tpl', model))

class DisplayWard(ModelAndViewPage):
	def get(self):
		if self.request.get('name'):
			wards = Ward.all().filter('name =', self.request.get('name')).fetch(limit=1)
			self.render('display', {'ward': wards[0] })
		else:
			self.render('display')

class Uploader(ModelAndViewPage):
	def get(self):
		self.render('upload')

	def post(self):
		ward = Ward(
			name=self.request.get('name'),
			district=self.request.get('district'),
			county=self.request.get('county'),
			urban_arts_eclectic=float(self.request.get('urban_arts_eclectic')),
			traditional_culture_vultures=float(self.request.get('traditional_culture_vultures')),
			fun_fashion_and_friends=float(self.request.get('fun_fashion_and_friends')),
			mature_explorers=float(self.request.get('mature_explorers')),
			dinner_and_a_show=float(self.request.get('dinner_and_a_show')),
			family_and_community_focused=float(self.request.get('family_and_community_focused')),
			bedroom_djs=float(self.request.get('bedroom_djs')),
			mid_life_hobbyists=float(self.request.get('mid-life_hobbyists')),
			retired_arts_and_crafts=float(self.request.get('retired_arts_and_crafts')),
			time_poor_dreamers=float(self.request.get('time_poor_dreamers')),
			a_quiet_pint_with_the_match=float(self.request.get('a_quiet_pint_with_the_match')),
			older_and_home_bound=float(self.request.get('older_and_home_bound'))
			)
		ward.put()
