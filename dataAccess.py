from sqlalchemy import create_engine, or_
from sqlalchemy.orm import sessionmaker, relationship
from models import Base, ParseResult

class Dao:
	session = None
	debug = False

	def __init__(self):
		engine = create_engine('sqlite:///huli.db', echo=False)
		Base.metadata.create_all(bind=engine)
		Session = sessionmaker(bind=engine) # <-- session factory
		self.session = Session()
		if (self.debug):
			print("*** Dao: new Session created *** MAKE SURE TO CALL THE \'close\' METHOD *** ")

	def set_debug(self, on_or_off):
		self.debug = on_or_off

	# --- PARSE RESULTS ---

	def getContent(self, search_term):
		return self.session.query(ParseResult)\
			.filter(or_(ParseResult.content.contains(search_term), ParseResult.keywords.contains(search_term)), ParseResult.scan_date != None)\
			.all()

	# --- CLEANUP ---

	def close(self):
		try:
			self.session.close()
			if self.debug:
				print('Dao: session closed cleanly')
		except AttributeError as error:
			# print(error)
			pass

if __name__ == '__main__':
	print('this is not a runable script')