Report: event({_from: indexed(address), _latitude: decimal, _longitude: decimal, _content: bytes64})

user: public({
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
         }[address])
	
@public
def isRegistered(addr: address) -> bool:
	return self.user[addr].enrolled

@public
def inputReport(_latitude: decimal, _longitude: decimal, _content: bytes64):
	assert self.user[msg.sender].enrolled 	# Throws if student is not yet enrolled
	log.Report(msg.sender, _latitude, _longitude, _content)  # log reporting event.

@public
def register(_first_name: bytes32, _last_name: bytes32):	
	assert not self.user[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.user[msg.sender].first_name = _first_name
	self.user[msg.sender].last_name = _last_name
	self.user[msg.sender].enrolled = True
