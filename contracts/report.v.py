user: public({
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
	bri: decimal, # Blockchain Report Index
         }[address])
	
report: public({
	longitude: num16,
	latitude: num16,
}[num][address])

cashier: public(address)
Report: __log__({latitude: num16, longitude: num16, arg3: indexed(address)})


def __init__(_cashier: address):
	self.owner = _cashier # Central authority

@public
def inputReport(_longitude, _latitude):
	assert self.user[msg.sender].enrolled 	# Throws if student is not yet enrolled
	self.report.longitude[bri][msg.sender] = _longitude
	self.report.latitude[bri][msg.sender] = _latitude
	self.user[msg.sender].bri += 1
	log.Report(_longitude, _latitude, msg.sender)

@public
@payable
def register(_first_name: bytes32, _last_name: bytes32):	
	assert not self.user[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.user[msg.sender].first_name = _first_name
	self.user[msg.sender].last_name = _last_name
	self.user[msg.sender].enrolled = True
	self.user[msg.sender].bri = 0
	
	
