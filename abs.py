import obd

# Establish a connection
connection = obd.OBD('/dev/cu.usbserial-210')

# Query basic engine trouble codes
cmd = obd.commands.GET_DTC
response = connection.query(cmd)

print('Engine/Emission GET_DTC')
print(response)
print(response.value)
print('')

# Check if there are manufacturer-specific codes available using extended diagnostics
# Send an ELM327 command to enter manufacturer-specific mode if needed
""" connection.send("ATSH7E0")  # Example: Set the OBD header (protocol dependent, common for Ford)
response = connection.query(cmd)

print('Ford Manufacturer GET_DTC')
print(response)
print(response.value)
print('') """

# Attempt to query specific modules (like ABS or Traction Control)
# This may require sending custom mode/commands if known for your vehicle
cmd = obd.commands.SERVICE_03  # OBD-II standard, can use for extended DTC query in some cases
response = connection.query(cmd)

print('Extended GET_DTC')
print(response)
print(response.value)
print('')
