# Update headers on WINDOW.BIN

import os
import binascii

########## HEADER1 ##########

# Open the file in write binary mode
f = open('HEADER1.BIN', 'wb')

# Go to first position
f.seek(0)

########## Compressed file ##########

# Get the size of compressed file 0_0 in bytes
compressed_file_00_size = os.path.getsize("WINDOW_0_0.GZ")

# Show it as an hex string (little-endian)
compressed_little_endian_00 = compressed_file_00_size.to_bytes(2, 'little').hex().upper()

print (compressed_little_endian_00)

# Write to the file
f.write(binascii.unhexlify(compressed_little_endian_00))

########## Uncompressed file ##########

# Get the size of uncompressed file 00 in bytes
uncompressed_file_00_size = os.path.getsize("WINDOW_0_0.data")

# Show it as an hex string (little-endian)
uncompressed_little_endian_00 = uncompressed_file_00_size.to_bytes(2, 'little').hex().upper()

print (uncompressed_little_endian_00)

# Write to the file
f.write(binascii.unhexlify(uncompressed_little_endian_00))

########## Append to the file ##########

# Write to the file
f.write(binascii.unhexlify('0000'))

# Close the file
f.close()

########## HEADER2 ##########

# Open the file in write binary mode
f = open('HEADER2.BIN', 'wb')

# Go to first position
f.seek(0)

########## Compressed file ##########

# Get the size of compressed file 0_1 in bytes
compressed_file_01_size = os.path.getsize("WINDOW_0_1.GZ")

# Show it as an hex string (little-endian)
compressed_little_endian_01 = compressed_file_01_size.to_bytes(2, 'little').hex().upper()

print (compressed_little_endian_01)

# Write to the file
f.write(binascii.unhexlify(compressed_little_endian_01))

########## Uncompressed file ##########

# Get the size of uncompressed file 01 in bytes
uncompressed_file_01_size = os.path.getsize("WINDOW_0_1.data")

# Show it as an hex string (little-endian)
uncompressed_little_endian_01 = uncompressed_file_01_size.to_bytes(2, 'little').hex().upper()

print (uncompressed_little_endian_01)

# Write to the file
f.write(binascii.unhexlify(uncompressed_little_endian_01))

########## Append to the file ##########

# Write to the file
f.write(binascii.unhexlify('0000'))

# Close the file
f.close()

########## HEADER3 ##########

# Open the file in write binary mode
f = open('HEADER3.BIN', 'wb')

# Go to first position
f.seek(0)

########## Compressed file ##########

# Get the size of compressed file 1_0 in bytes
compressed_file_10_size = os.path.getsize("WINDOW_1_0.GZ")

# Show it as an hex string (little-endian)
compressed_little_endian_10 = compressed_file_10_size.to_bytes(2, 'little').hex().upper()

print (compressed_little_endian_10)

# Write to the file
f.write(binascii.unhexlify(compressed_little_endian_10))

########## Uncompressed file ##########

# Get the size of uncompressed file 01 in bytes
uncompressed_file_10_size = os.path.getsize("WINDOW_1_0.data")

# Show it as an hex string (little-endian)
uncompressed_little_endian_10 = uncompressed_file_10_size.to_bytes(2, 'little').hex().upper()

print (uncompressed_little_endian_10)

# Write to the file
f.write(binascii.unhexlify(uncompressed_little_endian_10))

########## Append to the file ##########

# Write to the file
f.write(binascii.unhexlify('0100'))

# Close the file
f.close()

# End of file
