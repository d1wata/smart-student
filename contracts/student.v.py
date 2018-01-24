student: public({
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
         }[address])

report: public({
	longitude: num8,
	latitude: num8,
}[address][timestamp])

cashier: public(address)
reserve: num

def __init__(_cashier: address):
	self.owner = _cashier # Central authority
	
def inputReport(_grade: decimal, _subject: num, _year: num):
	assert self.student[msg.sender].enrolled 	# Throws if student is not yet enrolled
	self.student[msg.sender].grade[_year][_subject] = _grade

@payable
def register(_first_name: bytes32, _last_name: bytes32):	
	assert not self.student[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.student[msg.sender].first_name = _first_name
	self.student[msg.sender].last_name = _last_name
	self.student[msg.sender].enrolled = True
	
	
