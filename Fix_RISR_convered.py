import os

for filename in os.listdir('/Users/admin.e32063/Desktop/needs_two_zeros/'):
    if filename.startswith('RISR'):
        new = filename[:10] + '0' + filename[10] + '0' + filename[11:]
        print filename
        print new
        os.rename(filename, new)