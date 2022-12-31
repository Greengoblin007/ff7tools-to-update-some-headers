# 4-byte alignment for OPENING.BIN files

########## File 00 ##########

# Open the file in binary mode
f = open('OPENING_00.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_00.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 01 ##########

# Open the file in binary mode
f = open('OPENING_01.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_01.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 02 ##########

# Open the file in binary mode
f = open('OPENING_02.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_02.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 03 ##########

# Open the file in binary mode
f = open('OPENING_03.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_03.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 04 ##########

# Open the file in binary mode
f = open('OPENING_04.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_04.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 05 ##########

# Open the file in binary mode
f = open('OPENING_05.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_05.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 06 ##########

# Open the file in binary mode
f = open('OPENING_06.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_06.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 07 ##########

# Open the file in binary mode
f = open('OPENING_07.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_07.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 17 ##########

# Open the file in binary mode
f = open('OPENING_17.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_17.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 18 ##########

# Open the file in binary mode
f = open('OPENING_18.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_18.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

########## File 21 ##########

# Open the file in binary mode
f = open('OPENING_21.LZS', 'rb')

# Read the entire file into memory
data = f.read()

# Go to first position
f.seek(0)

# Calculate the number of bytes needed to align the data to 4-byte boundaries
alignment = (4 - (len(data) % 4)) % 4

# Add padding to the end of the data to ensure 4-byte alignment
data += b'\x00' * alignment

# Write the aligned data back to the file
with open('OPENING_21.LZS', 'wb') as f:
    f.write(data)

# Close the file
f.close()

# End of file
