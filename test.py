import obd

# Connect to the OBD-II port
connection = obd.OBD('/dev/cu.usbserial-10')

# Clear the trouble codes
clear_command = obd.commands.CLEAR_DTC  # Command to clear trouble codes
response = connection.query(clear_command)  # Send the command

print(response)