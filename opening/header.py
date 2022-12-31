# Update headers on file OPENING.BIN

import os
import binascii

########## Insert 5C ##########

# Open the file in read/write mode
f = open('HEADER.BIN', 'wb')

# Go to first position
f.seek(0)

# Write to the file
f.write(binascii.unhexlify('5C000000'))

########## File 00 ##########

# Get the size of file 00 in bytes
file_00_size = os.path.getsize("OPENING_00.LZS")

# 0x5C + file_00_size
modified_file_00_size = 0x5C + file_00_size

# Show it as a hex string (little-endian)
little_endian_00 = modified_file_00_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_00))

########## File 01 ##########

# Get the size of file 01 in bytes
file_01_size = os.path.getsize("OPENING_01.LZS")

# 0x5C + all previous files + actual file
modified_file_01_size = modified_file_00_size + file_01_size

# Show it as a hex string (little-endian)
little_endian_01 = modified_file_01_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_01))

########## File 02 ##########

# Get the size of file 02 in bytes
file_02_size = os.path.getsize("OPENING_02.LZS")

# 0x5C + all previous files + actual file
modified_file_02_size = modified_file_01_size + file_02_size

# Show it as a hex string (little-endian)
little_endian_02 = modified_file_02_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_02))

########## File 03 ##########

# Get the size of file 03 in bytes
file_03_size = os.path.getsize("OPENING_03.LZS")

# 0x5C + all previous files + actual file
modified_file_03_size = modified_file_02_size + file_03_size

# Show it as a hex string (little-endian)
little_endian_03 = modified_file_03_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_03))

########## File 04 ##########

# Get the size of file 04 in bytes
file_04_size = os.path.getsize("OPENING_04.LZS")

# 0x5C + all previous files + actual file
modified_file_04_size = modified_file_03_size + file_04_size

# Show it as a hex string (little-endian)
little_endian_04 = modified_file_04_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_04))

########## File 05 ##########

# Get the size of file 05 in bytes
file_05_size = os.path.getsize("OPENING_05.LZS")

# 0x5C + all previous files + actual file
modified_file_05_size = modified_file_04_size + file_05_size

# Show it as a hex string (little-endian)
little_endian_05 = modified_file_05_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_05))

########## File 06 ##########

# Get the size of file 06 in bytes
file_06_size = os.path.getsize("OPENING_06.LZS")

# 0x5C + all previous files + actual file
modified_file_06_size = modified_file_05_size + file_06_size

# Show it as a hex string (little-endian)
little_endian_06 = modified_file_06_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_06))

########## File 07 ##########

# Get the size of file 07 in bytes
file_07_size = os.path.getsize("OPENING_07.LZS")

# 0x5C + all previous files + actual file
modified_file_07_size = modified_file_06_size + file_07_size

# Show it as a hex string (little-endian)
little_endian_07 = modified_file_07_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_07))

########## File 08 ##########

# Get the size of file 08 in bytes
file_08_size = os.path.getsize("OPENING_08.DATA")

# 0x5C + all previous files + actual file
modified_file_08_size = modified_file_07_size + file_08_size

# Show it as a hex string (little-endian)
little_endian_08 = modified_file_08_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_08))

########## File 09 ##########

# Get the size of file 09 in bytes
file_09_size = os.path.getsize("OPENING_09.DATA")

# 0x5C + all previous files + actual file
modified_file_09_size = modified_file_08_size + file_09_size

# Show it as a hex string (little-endian)
little_endian_09 = modified_file_09_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_09))

########## File 10 ##########

# Get the size of file 10 in bytes
file_10_size = os.path.getsize("OPENING_10.DATA")

# 0x5C + all previous files + actual file
modified_file_10_size = modified_file_09_size + file_10_size

# Show it as a hex string (little-endian)
little_endian_10 = modified_file_10_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_10))

########## File 11 ##########

# Get the size of file 11 in bytes
file_11_size = os.path.getsize("OPENING_11.DATA")

# 0x5C + all previous files + actual file
modified_file_11_size = modified_file_10_size + file_11_size

# Show it as a hex string (little-endian)
little_endian_11 = modified_file_11_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_11))

########## File 12 ##########

# Get the size of file 12 in bytes
file_12_size = os.path.getsize("OPENING_12.DATA")

# 0x5C + all previous files + actual file
modified_file_12_size = modified_file_11_size + file_12_size

# Show it as a hex string (little-endian)
little_endian_12 = modified_file_12_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_12))

########## File 13 ##########

# Get the size of file 13 in bytes
file_13_size = os.path.getsize("OPENING_13.DATA")

# 0x5C + all previous files + actual file
modified_file_13_size = modified_file_12_size + file_13_size

# Show it as a hex string (little-endian)
little_endian_13 = modified_file_13_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_13))

########## File 14 ##########

# Get the size of file 14 in bytes
file_14_size = os.path.getsize("OPENING_14.DATA")

# 0x5C + all previous files + actual file
modified_file_14_size = modified_file_13_size + file_14_size

# Show it as a hex string (little-endian)
little_endian_14 = modified_file_14_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_14))

########## File 15 ##########

# Get the size of file 15 in bytes
file_15_size = os.path.getsize("OPENING_15.DATA")

# 0x5C + all previous files + actual file
modified_file_15_size = modified_file_14_size + file_15_size

# Show it as a hex string (little-endian)
little_endian_15 = modified_file_15_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_15))

########## File 16 ##########

# Get the size of file 16 in bytes
file_16_size = os.path.getsize("OPENING_16.DATA")

# 0x5C + all previous files + actual file
modified_file_16_size = modified_file_15_size + file_16_size

# Show it as a hex string (little-endian)
little_endian_16 = modified_file_16_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_16))

########## File 17 ##########

# Get the size of file 17 in bytes
file_17_size = os.path.getsize("OPENING_17.LZS")

# 0x5C + all previous files + actual file
modified_file_17_size = modified_file_16_size + file_17_size

# Show it as a hex string (little-endian)
little_endian_17 = modified_file_17_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_17))

########## File 18 ##########

# Get the size of file 18 in bytes
file_18_size = os.path.getsize("OPENING_18.LZS")

# 0x5C + all previous files + actual file
modified_file_18_size = modified_file_17_size + file_18_size

# Show it as a hex string (little-endian)
little_endian_18 = modified_file_18_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_18))

########## File 19 ##########

# Get the size of file 19 in bytes
file_19_size = os.path.getsize("OPENING_19.DATA")

# 0x5C + all previous files + actual file
modified_file_19_size = modified_file_18_size + file_19_size

# Show it as a hex string (little-endian)
little_endian_19 = modified_file_19_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_19))

########## File 20 ##########

# Get the size of file 20 in bytes
file_20_size = os.path.getsize("OPENING_20.DATA")

# 0x5C + all previous files + actual file
modified_file_20_size = modified_file_19_size + file_20_size

# Show it as a hex string (little-endian)
little_endian_20 = modified_file_20_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_20))

########## File 21 ##########

# Get the size of file 21 in bytes
file_21_size = os.path.getsize("OPENING_21.LZS")

# 0x5C + all previous files + actual file
modified_file_21_size = modified_file_20_size + file_21_size

# Show it as a hex string (little-endian)
little_endian_21 = modified_file_21_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_21))

# Close the file
f.close()

# End of file
