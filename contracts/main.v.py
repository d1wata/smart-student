student: {
  balance: currency_value, # cashier issued Philippine Peso-pegged token for e-transaction in PSHS
  id_num: bytes32, # Registrar specified Id number (e.g. "13-6363623")
	enrolled: bool,
	first_name: bytes32, # Legal first name
	last_name: bytes32, # Legal last name
	grade: num[6][8] # [year][subject number code]
         }[address]

cashier: address
reserve: num


def __init__(_cashier: address):
	self.cashier = _cashier # Central token authority
	self.reserve = 100000 # 100,000 Pesos Starting Cash Reserve

@payable
def register(_id_num: bytes32, _first_name: bytes32, _last_name: bytes32):	
	assert not self.student[msg.sender].enrolled # Throws if user is already enrolled
	
	self.student[msg.sender].id_num = _id_num
	self.student[msg.sender].first_name = _first_name
	self.student[msg.sender].last_name = _last_name
	self.student[msg.sender].enrolled = True
	
def issuePeso(_amount: num, _to: address):
	assert msg.sender == self.cashier # Throws if user is not the cashier
	self.reserve += _amount # Add _amount to current reserve
	
	

  
