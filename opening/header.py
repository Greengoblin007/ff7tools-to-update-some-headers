# Update headers on file OPENING.BIN

import os
import binascii

########## Insert 5C ##########

# Open the file in write binary mode
f = open('HEADER.BIN', 'wb')

# Go to first position
f.seek(0)

# Write to the file
f.write(binascii.unhexlify('5C000000'))

# Set initial offset
initial_offset = 0x5C

path = os.getcwd() # current directory
for filename in os.listdir(path): # all files in current directory
    if filename.endswith((".LZS", ".data")): # only .LZS and .data files

        # Open the file in append binary mode
        with open(filename, 'ab') as f:

            # Get the size of file in bytes
            file_size = os.path.getsize(filename)

            # Offset
            initial_offset += file_size

            # Show it as an hex string (little-endian)
            little_endian = initial_offset.to_bytes(4, 'little').hex().upper()

            print (little_endian)

            # Open HEADER file in append binary mode
            with open('HEADER.BIN', 'ab') as f:
                f.write(binascii.unhexlify(little_endian))

            # Close the file
            f.close()

# Open the file in read binary mode
with open('HEADER.BIN', 'rb') as f:

    # Read the binary file into a bytearray
    data = bytearray(f.read())

    # Remove the bytes you want to delete
    del data[0x5C : 0x5C + 4]

    # Open HEADER file in write binary mode
    with open('HEADER.BIN', 'wb') as f:

    # Write the remaining bytes back to the file
        f.write(data)

    # Close the file
    f.close()

# End of file
