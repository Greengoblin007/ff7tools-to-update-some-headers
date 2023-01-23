# Update headers on file STAFF2.BIN

import os
import binascii

########## Insert BC ##########

# Open the file in write binary mode
f = open('HEADER.BIN', 'wb')

# Go to first position
f.seek(0)

# Write to the file
f.write(binascii.unhexlify('BC000000'))

########## Insert remaining offsets ##########

# Set initial offset
initial_offset = 0xBC

path = os.getcwd() # current directory
for filename in os.listdir(path): # all files in current directory
    if filename.endswith((".LZS", ".data")): # only .LZS and .data files

        # Open the file in append binary mode
        with open(filename, 'ab') as f:

            # Get the size of file in bytes
            file_size = os.path.getsize(filename)
            
            # Calculate offset
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
    del data[0xBC : 0xBC + 4]

    # Open HEADER file in write binary mode
    with open('HEADER.BIN', 'wb') as f:

    # Write the remaining bytes back to the file
        f.write(data)

    # Close the file
    f.close()

# End of file
