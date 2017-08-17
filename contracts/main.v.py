student: public({
  balance: currency_value, # cashier issued Philippine Peso-pegged token for e-transaction in PSHS
  id_num: bytes32, # Registrar specified Id number (e.g. "13-63623")
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
	grade: decimal[6][8] # [year][subject number code]
         }[address])

cashier: public(address)
reserve: num

def __init__(_cashier: address):
	self.cashier = _cashier # Central token authority
	self.reserve = 0 	# 100,000 Pesos Starting Cash Reserve
	
def setFinalGrade(_grade: decimal, _subject: num, _year: num):
	assert self.student[msg.sender].enrolled 	# Throws if student is not yet enrolled
	self.student[msg.sender].grade[_year][_subject] = _grade

@payable
def register(_id_num: bytes32, _first_name: bytes32, _last_name: bytes32):	
	assert not self.student[msg.sender].enrolled    # Throws if user is already enrolled
	
	# Adding identity data
	self.student[msg.sender].id_num = _id_num
	self.student[msg.sender].first_name = _first_name
	self.student[msg.sender].last_name = _last_name
	self.student[msg.sender].enrolled = True
	
def issuePeso(_amount: num, _to: address):
	assert msg.sender == self.cashier # Throws if user is not the cashier
	self.reserve += _amount 	  # Add _amount to current reserve
	
def transfer(_to: address, _amount: currency_value):
	assert self.student[msg.sender].balance >= _amount 	# Throw if send amount greater than balance
		  
	self.student[msg.sender].balance -= _amount
	self.student[_to].balance += _amount
	
