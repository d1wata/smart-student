Report: __log__({_from: indexed(address), _latitude: indexed(num256), _longitude: indexed(num256)})

user: public({
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
         }[address])

owner: address

@public
def __init__(_administrator: address):
	self.owner = _administrator # Central authority

@public
def inputReport(_latitude: num256, _longitude: num256):
	assert self.user[msg.sender].enrolled 	# Throws if student is not yet enrolled
	log.Report(msg.sender, _latitude, _longitude)  # log reporting event.

@public
@payable
def register(_first_name: bytes32, _last_name: bytes32):	
	assert not self.user[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.user[msg.sender].first_name = _first_name
	self.user[msg.sender].last_name = _last_name
	self.user[msg.sender].enrolled = True
