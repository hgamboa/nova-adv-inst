from get_stats import get_stats
import tornado.ioloop
import tornado.web

# This class will be called when you visit or make a GET request
# to http:RASPIP:8888/ and returns 'Alive' to said request.
class HeartHandler(tornado.web.RequestHandler):
	def get(self):
		self.write('Alive')

# This class will be called when you visit or make a GET request
# to http:RASPIP:8888/stats. It will then run the get_stats function
# from get_stats.py file and return the result to said request.
class StatsHandler(tornado.web.RequestHandler):
	def get(self):
		interval = 0.5
		try:
			# If you got http:RASPIP:8888/stats?interval=(insert float)
			# instead, you will change the polling interval to measure
			# the CPU load.
			interval = float(self.get_argument('interval', None))
		except:
			pass
		self.write(get_stats(interval))

def make_app():
	# The return statment of this function is what makes the web addresses
	# to the classes define above. r'/' is connected to HeartHandler while
	# r'/stats' is connected to StatsHandler. This is called routing
	return tornado.web.Application([(r"/", HeartHandler),
		(r"/stats", StatsHandler),
	])

if __name__ == "__main__":
	app = make_app() # This configures our web server routes
	app.listen(8888) # We map port 8888 to our server
	tornado.ioloop.IOLoop.current().start() # We start our server


