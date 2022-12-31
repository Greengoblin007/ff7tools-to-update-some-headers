# Update headers on file STAFF2.BIN

import os
import binascii

########## Insert 5C ##########

# Open the file in read/write mode
f = open('HEADER.BIN', 'wb')

# Go to first position
f.seek(0)

# Write to the file
f.write(binascii.unhexlify('BC000000'))

########## File 00 ##########

# Get the size of file 00 in bytes
file_00_size = os.path.getsize("STAFF2_00.LZS")

# 0x5C + file_00_size
modified_file_00_size = 0xBC + file_00_size

# Show it as a hex string (little-endian)
little_endian_00 = modified_file_00_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_00))

########## File 01 ##########

# Get the size of file 01 in bytes
file_01_size = os.path.getsize("STAFF2_01.LZS")

# 0x5C + all previous files + actual file
modified_file_01_size = modified_file_00_size + file_01_size

# Show it as a hex string (little-endian)
little_endian_01 = modified_file_01_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_01))

########## File 02 ##########

# Get the size of file 02 in bytes
file_02_size = os.path.getsize("STAFF2_02.LZS")

# 0x5C + all previous files + actual file
modified_file_02_size = modified_file_01_size + file_02_size

# Show it as a hex string (little-endian)
little_endian_02 = modified_file_02_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_02))

########## File 03 ##########

# Get the size of file 03 in bytes
file_03_size = os.path.getsize("STAFF2_03.LZS")

# 0x5C + all previous files + actual file
modified_file_03_size = modified_file_02_size + file_03_size

# Show it as a hex string (little-endian)
little_endian_03 = modified_file_03_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_03))

########## File 04 ##########

# Get the size of file 04 in bytes
file_04_size = os.path.getsize("STAFF2_04.LZS")

# 0x5C + all previous files + actual file
modified_file_04_size = modified_file_03_size + file_04_size

# Show it as a hex string (little-endian)
little_endian_04 = modified_file_04_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_04))

########## File 05 ##########

# Get the size of file 05 in bytes
file_05_size = os.path.getsize("STAFF2_05.LZS")

# 0x5C + all previous files + actual file
modified_file_05_size = modified_file_04_size + file_05_size

# Show it as a hex string (little-endian)
little_endian_05 = modified_file_05_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_05))

########## File 06 ##########

# Get the size of file 06 in bytes
file_06_size = os.path.getsize("STAFF2_06.LZS")

# 0x5C + all previous files + actual file
modified_file_06_size = modified_file_05_size + file_06_size

# Show it as a hex string (little-endian)
little_endian_06 = modified_file_06_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_06))

########## File 07 ##########

# Get the size of file 07 in bytes
file_07_size = os.path.getsize("STAFF2_07.LZS")

# 0x5C + all previous files + actual file
modified_file_07_size = modified_file_06_size + file_07_size

# Show it as a hex string (little-endian)
little_endian_07 = modified_file_07_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_07))

########## File 08 ##########

# Get the size of file 08 in bytes
file_08_size = os.path.getsize("STAFF2_08.LZS")

# 0x5C + all previous files + actual file
modified_file_08_size = modified_file_07_size + file_08_size

# Show it as a hex string (little-endian)
little_endian_08 = modified_file_08_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_08))

########## File 09 ##########

# Get the size of file 09 in bytes
file_09_size = os.path.getsize("STAFF2_09.LZS")

# 0x5C + all previous files + actual file
modified_file_09_size = modified_file_08_size + file_09_size

# Show it as a hex string (little-endian)
little_endian_09 = modified_file_09_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_09))

########## File 10 ##########

# Get the size of file 10 in bytes
file_10_size = os.path.getsize("STAFF2_10.LZS")

# 0x5C + all previous files + actual file
modified_file_10_size = modified_file_09_size + file_10_size

# Show it as a hex string (little-endian)
little_endian_10 = modified_file_10_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_10))

########## File 11 ##########

# Get the size of file 11 in bytes
file_11_size = os.path.getsize("STAFF2_11.LZS")

# 0x5C + all previous files + actual file
modified_file_11_size = modified_file_10_size + file_11_size

# Show it as a hex string (little-endian)
little_endian_11 = modified_file_11_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_11))

########## File 12 ##########

# Get the size of file 12 in bytes
file_12_size = os.path.getsize("STAFF2_12.LZS")

# 0x5C + all previous files + actual file
modified_file_12_size = modified_file_11_size + file_12_size

# Show it as a hex string (little-endian)
little_endian_12 = modified_file_12_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_12))

########## File 13 ##########

# Get the size of file 13 in bytes
file_13_size = os.path.getsize("STAFF2_13.LZS")

# 0x5C + all previous files + actual file
modified_file_13_size = modified_file_12_size + file_13_size

# Show it as a hex string (little-endian)
little_endian_13 = modified_file_13_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_13))

########## File 14 ##########

# Get the size of file 14 in bytes
file_14_size = os.path.getsize("STAFF2_14.LZS")

# 0x5C + all previous files + actual file
modified_file_14_size = modified_file_13_size + file_14_size

# Show it as a hex string (little-endian)
little_endian_14 = modified_file_14_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_14))

########## File 15 ##########

# Get the size of file 15 in bytes
file_15_size = os.path.getsize("STAFF2_15.LZS")

# 0x5C + all previous files + actual file
modified_file_15_size = modified_file_14_size + file_15_size

# Show it as a hex string (little-endian)
little_endian_15 = modified_file_15_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_15))

########## File 16 ##########

# Get the size of file 16 in bytes
file_16_size = os.path.getsize("STAFF2_16.LZS")

# 0x5C + all previous files + actual file
modified_file_16_size = modified_file_15_size + file_16_size

# Show it as a hex string (little-endian)
little_endian_16 = modified_file_16_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_16))

########## File 17 ##########

# Get the size of file 17 in bytes
file_17_size = os.path.getsize("STAFF2_17.LZS")

# 0x5C + all previous files + actual file
modified_file_17_size = modified_file_16_size + file_17_size

# Show it as a hex string (little-endian)
little_endian_17 = modified_file_17_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_17))

########## File 18 ##########

# Get the size of file 18 in bytes
file_18_size = os.path.getsize("STAFF2_18.LZS")

# 0x5C + all previous files + actual file
modified_file_18_size = modified_file_17_size + file_18_size

# Show it as a hex string (little-endian)
little_endian_18 = modified_file_18_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_18))

########## File 19 ##########

# Get the size of file 19 in bytes
file_19_size = os.path.getsize("STAFF2_19.LZS")

# 0x5C + all previous files + actual file
modified_file_19_size = modified_file_18_size + file_19_size

# Show it as a hex string (little-endian)
little_endian_19 = modified_file_19_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_19))

########## File 20 ##########

# Get the size of file 20 in bytes
file_20_size = os.path.getsize("STAFF2_20.LZS")

# 0x5C + all previous files + actual file
modified_file_20_size = modified_file_19_size + file_20_size

# Show it as a hex string (little-endian)
little_endian_20 = modified_file_20_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_20))

########## File 21 ##########

# Get the size of file 21 in bytes
file_21_size = os.path.getsize("STAFF2_21.DATA")

# 0x5C + all previous files + actual file
modified_file_21_size = modified_file_20_size + file_21_size

# Show it as a hex string (little-endian)
little_endian_21 = modified_file_21_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_21))

########## File 22 ##########

# Get the size of file 22 in bytes
file_22_size = os.path.getsize("STAFF2_22.DATA")

# 0x5C + all previous files + actual file
modified_file_22_size = modified_file_21_size + file_22_size

# Show it as a hex string (little-endian)
little_endian_22 = modified_file_22_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_22))

########## File 23 ##########

# Get the size of file 23 in bytes
file_23_size = os.path.getsize("STAFF2_23.DATA")

# 0x5C + all previous files + actual file
modified_file_23_size = modified_file_22_size + file_23_size

# Show it as a hex string (little-endian)
little_endian_23 = modified_file_23_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_23))

########## File 24 ##########

# Get the size of file 24 in bytes
file_24_size = os.path.getsize("STAFF2_24.DATA")

# 0x5C + all previous files + actual file
modified_file_24_size = modified_file_23_size + file_24_size

# Show it as a hex string (little-endian)
little_endian_24 = modified_file_24_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_24))

########## File 25 ##########

# Get the size of file 25 in bytes
file_25_size = os.path.getsize("STAFF2_25.DATA")

# 0x5C + all previous files + actual file
modified_file_25_size = modified_file_24_size + file_25_size

# Show it as a hex string (little-endian)
little_endian_25 = modified_file_25_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_25))

########## File 26 ##########

# Get the size of file 26 in bytes
file_26_size = os.path.getsize("STAFF2_26.DATA")

# 0x5C + all previous files + actual file
modified_file_26_size = modified_file_25_size + file_26_size

# Show it as a hex string (little-endian)
little_endian_26 = modified_file_26_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_26))

########## File 27 ##########

# Get the size of file 27 in bytes
file_27_size = os.path.getsize("STAFF2_27.DATA")

# 0x5C + all previous files + actual file
modified_file_27_size = modified_file_26_size + file_27_size

# Show it as a hex string (little-endian)
little_endian_27 = modified_file_27_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_27))

########## File 28 ##########

# Get the size of file 28 in bytes
file_28_size = os.path.getsize("STAFF2_28.DATA")

# 0x5C + all previous files + actual file
modified_file_28_size = modified_file_27_size + file_28_size

# Show it as a hex string (little-endian)
little_endian_28 = modified_file_28_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_28))

########## File 29 ##########

# Get the size of file 29 in bytes
file_29_size = os.path.getsize("STAFF2_29.DATA")

# 0x5C + all previous files + actual file
modified_file_29_size = modified_file_28_size + file_29_size

# Show it as a hex string (little-endian)
little_endian_29 = modified_file_29_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_29))

########## File 30 ##########

# Get the size of file 30 in bytes
file_30_size = os.path.getsize("STAFF2_30.DATA")

# 0x5C + all previous files + actual file
modified_file_30_size = modified_file_29_size + file_30_size

# Show it as a hex string (little-endian)
little_endian_30 = modified_file_30_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_30))

########## File 31 ##########

# Get the size of file 31 in bytes
file_31_size = os.path.getsize("STAFF2_31.DATA")

# 0x5C + all previous files + actual file
modified_file_31_size = modified_file_30_size + file_31_size

# Show it as a hex string (little-endian)
little_endian_31 = modified_file_31_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_31))

########## File 32 ##########

# Get the size of file 32 in bytes
file_32_size = os.path.getsize("STAFF2_32.DATA")

# 0x5C + all previous files + actual file
modified_file_32_size = modified_file_31_size + file_32_size

# Show it as a hex string (little-endian)
little_endian_32 = modified_file_32_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_32))

########## File 33 ##########

# Get the size of file 33 in bytes
file_33_size = os.path.getsize("STAFF2_33.DATA")

# 0x5C + all previous files + actual file
modified_file_33_size = modified_file_32_size + file_33_size

# Show it as a hex string (little-endian)
little_endian_33 = modified_file_33_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_33))

########## File 34 ##########

# Get the size of file 34 in bytes
file_34_size = os.path.getsize("STAFF2_34.DATA")

# 0x5C + all previous files + actual file
modified_file_34_size = modified_file_33_size + file_34_size

# Show it as a hex string (little-endian)
little_endian_34 = modified_file_34_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_34))

########## File 35 ##########

# Get the size of file 35 in bytes
file_35_size = os.path.getsize("STAFF2_35.DATA")

# 0x5C + all previous files + actual file
modified_file_35_size = modified_file_34_size + file_35_size

# Show it as a hex string (little-endian)
little_endian_35 = modified_file_35_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_35))

########## File 36 ##########

# Get the size of file 36 in bytes
file_36_size = os.path.getsize("STAFF2_36.DATA")

# 0x5C + all previous files + actual file
modified_file_36_size = modified_file_35_size + file_36_size

# Show it as a hex string (little-endian)
little_endian_36 = modified_file_36_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_36))

########## File 37 ##########

# Get the size of file 37 in bytes
file_37_size = os.path.getsize("STAFF2_37.DATA")

# 0x5C + all previous files + actual file
modified_file_37_size = modified_file_36_size + file_37_size

# Show it as a hex string (little-endian)
little_endian_37 = modified_file_37_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_37))

########## File 38 ##########

# Get the size of file 38 in bytes
file_38_size = os.path.getsize("STAFF2_38.DATA")

# 0x5C + all previous files + actual file
modified_file_38_size = modified_file_37_size + file_38_size

# Show it as a hex string (little-endian)
little_endian_38 = modified_file_38_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_38))

########## File 39 ##########

# Get the size of file 39 in bytes
file_39_size = os.path.getsize("STAFF2_39.DATA")

# 0x5C + all previous files + actual file
modified_file_39_size = modified_file_38_size + file_39_size

# Show it as a hex string (little-endian)
little_endian_39 = modified_file_39_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_39))

########## File 40 ##########

# Get the size of file 40 in bytes
file_40_size = os.path.getsize("STAFF2_40.DATA")

# 0x5C + all previous files + actual file
modified_file_40_size = modified_file_39_size + file_40_size

# Show it as a hex string (little-endian)
little_endian_40 = modified_file_40_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_40))

########## File 41 ##########

# Get the size of file 41 in bytes
file_41_size = os.path.getsize("STAFF2_41.DATA")

# 0x5C + all previous files + actual file
modified_file_41_size = modified_file_40_size + file_41_size

# Show it as a hex string (little-endian)
little_endian_41 = modified_file_41_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_41))

########## File 42 ##########

# Get the size of file 42 in bytes
file_42_size = os.path.getsize("STAFF2_42.DATA")

# 0x5C + all previous files + actual file
modified_file_42_size = modified_file_41_size + file_42_size

# Show it as a hex string (little-endian)
little_endian_42 = modified_file_42_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_42))

########## File 43 ##########

# Get the size of file 43 in bytes
file_43_size = os.path.getsize("STAFF2_43.LZS")

# 0x5C + all previous files + actual file
modified_file_43_size = modified_file_42_size + file_43_size

# Show it as a hex string (little-endian)
little_endian_43 = modified_file_43_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_43))

########## File 44 ##########

# Get the size of file 44 in bytes
file_44_size = os.path.getsize("STAFF2_44.DATA")

# 0x5C + all previous files + actual file
modified_file_44_size = modified_file_43_size + file_44_size

# Show it as a hex string (little-endian)
little_endian_44 = modified_file_44_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_44))

########## File 45 ##########

# Get the size of file 45 in bytes
file_45_size = os.path.getsize("STAFF2_45.DATA")

# 0x5C + all previous files + actual file
modified_file_45_size = modified_file_44_size + file_45_size

# Show it as a hex string (little-endian)
little_endian_45 = modified_file_45_size.to_bytes(4, 'little').hex().upper()

# Write to the file
f.write(binascii.unhexlify(little_endian_45))

# Close the file
f.close()

# End of file
