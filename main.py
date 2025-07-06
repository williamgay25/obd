import obd

connection = obd.OBD('/dev/cu.usbserial-210')

# Get the speed to test
cmd = obd.commands.SPEED  
response = connection.query(cmd)

print(response.value)
print(response.value.to("mph"))

""" # Clear the trouble codes
clear_command = obd.commands.CLEAR_DTC
response = connection.query(clear_command)

# should print none
print("CLEAR_DTC")
print(response)
print(response.value)
print('') """

cmd = obd.commands.GET_CURRENT_DTC
response = connection.query(cmd)

print('GET_CURRENT_DTC')
print(response)
print(response.value)
print('')

cmd = obd.commands.GET_DTC
response = connection.query(cmd)

print('GET_DTC')
print(response)
print(response.value)

# Commands
# https://python-obd.readthedocs.io/en/latest/Command%20Tables/

# Expedition DTC 
""" 

python main.py
GET_CURRENT_DTC
[('P0303', 'Cylinder 3 Misfire Detected'), ('P0353', "Ignition Coil 'C' Primary/Secondary Circuit")]
[('P0303', 'Cylinder 3 Misfire Detected'), ('P0353', "Ignition Coil 'C' Primary/Secondary Circuit")]

GET_DTC
[('P0303', 'Cylinder 3 Misfire Detected'), ('P0353', "Ignition Coil 'C' Primary/Secondary Circuit")]
[('P0303', 'Cylinder 3 Misfire Detected'), ('P0353', "Ignition Coil 'C' Primary/Secondary Circuit")]

 """