# Update headers on file STAFF2.BIN

import os
import binascii

########## Insert BC ##########

# Open the file in read/write mode
f = open('HEADER.BIN', 'wb')

# Go to first position
f.seek(0)

# Write to the file
f.write(binascii.unhexlify('BC000000'))

initial_offset = 0xBC

path = os.getcwd() # current directory
for filename in os.listdir(path):
    if filename.endswith((".LZS", ".data")):
        with open(filename, 'ab') as f:

            # Get the size of file in bytes
            file_size = os.path.getsize(filename)
            
            # Offset
            initial_offset += file_size

            # Show it as an hex string (little-endian)
            little_endian = initial_offset.to_bytes(4, 'little').hex().upper()
            print (little_endian)

            with open('HEADER.BIN', 'ab') as f:
                f.write(binascii.unhexlify(little_endian))

            # Close the file
            f.close()

with open('HEADER.BIN', 'rb') as f:
    # Read the binary file into a bytearray
    data = bytearray(f.read())

    # Remove the bytes you want to delete
    del data[0xBC : 0xBC + 4]

    with open('HEADER.BIN', 'wb') as f:
    # Write the remaining bytes back to the file
        f.write(data)

    # Close the file
    f.close()

# End of file
