user: public({
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
         }[address])

	
Report: __log__({_from: indexed(address), _latitude: num256, _longitude: num256})


def __init__(_administrator: address):
	self.owner = _administrator # Central authority
	
def inputReport(_latitude, _longitude):
	assert self.user[msg.sender].enrolled 	# Throws if student is not yet enrolled
	self.user[msg.sender]
	log.Report(msg.sender, convert(_latitude, 'num256'), convert(_longitude, 'num256'))  # log reporting event.
	
def upgradeContract(_contract):
	# work in progress code to upgrade contract after final implementation


@payable
def register(_first_name: bytes32, _last_name: bytes32):	
	assert not self.user[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.user[msg.sender].first_name = _first_name
	self.user[msg.sender].last_name = _last_name
	self.user[msg.sender].enrolled = True
	
	
