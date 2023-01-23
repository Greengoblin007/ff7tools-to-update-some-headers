# 4-byte alignment for STAFF2.BIN files

import os

path = os.getcwd() # current directory
for filename in os.listdir(path): # all files in current directory
    if filename.endswith(".LZS"): # only .LZS files

        # Open the file in read binary mode
        with open(filename, 'rb') as f:

            # Read the entire file into memory
            data = f.read()

            # Go to first position
            f.seek(0)

            # Calculate the number of bytes needed to align the data to 4-byte boundaries
            alignment = (4 - (len(data) % 4)) % 4

            # Add padding to the end of the data to ensure 4-byte alignment
            data += b'\x00' * alignment

            # Write the aligned data back to the file (write binary mode)
            with open(filename, 'wb') as f:
                f.write(data)

            # Close the file
            f.close()

# End of file
