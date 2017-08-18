student: public({
	# Student Meta Data
	
  	id_num: bytes32, # Registrar specified Id number (e.g. "13-63623")
	enrolled: bool,
	
	# Student Profile Data
	
	first_name: bytes32,
	last_name: bytes32,
	
	# Student Dynamic Data
	
	time_in: timestamp,
	time_out: timestamp
	
         }[address])

	
@payable
def checkIn(_time_in: timestamp):
	self.student[msg.sender].time_in: _time_in

@payable
def checkOut(_time_out: timestamp):
	self.student[msg.sender].time_out: _time_out

@payable
def enroll(_id_num: bytes32, _first_name: bytes32, _last_name: bytes32):	
	assert not self.student[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.student[msg.sender].id_num = _id_num
	self.student[msg.sender].first_name = _first_name
	self.student[msg.sender].last_name = _last_name
	self.student[msg.sender].enrolled = True
	
