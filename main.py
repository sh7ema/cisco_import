import os
import shutil
import glob


# Scan directory for zip
file_dir = glob.glob('./*.zip')

# In local directory you have one zip
# Put name of zip to variable
filename = file_dir[0]

# Create folder for unzip
extract_dir = './test1'

# Create path for users with '*.pka'.
extract_dir1 = './part1'
extract_dir2 = './part2'
extract_dir3 = './part3'

# If group > 30 peoples, create 'extract_dir4'
# extract_dir4 = './part4'

# Create directory, where you unzip
os.makedirs(extract_dir)

# Create folders for files with '*.pka'
os.makedirs(extract_dir1)
os.makedirs(extract_dir2)
os.makedirs(extract_dir3)
# os.makedirs(extract_dir4)

# Unzip archive to directory test1
shutil.unpack_archive(filename, extract_dir)

# Give user's list for next len
get_files = os.listdir(extract_dir)

counter = 0

# Find files with extension '.pka' and move to folder part1 ... part3
for filename in glob.glob("./test1/*/*.pka"):
    if counter < 10:
        shutil.move(filename, extract_dir1)
    elif counter < 20:
        shutil.move(filename, extract_dir2)
    # For 40 peoples
    # elif counter < 30:
    #     shutil.move(filename, extract_dir3)
    else:
        shutil.move(filename, extract_dir3)
        # Delete previous code
        # shutil.move(filename, extract_dir4)
    counter += 1

# Delete extra directory
if len(get_files) < 10:
    shutil.rmtree(extract_dir2)
    shutil.rmtree(extract_dir3)
if len(get_files) < 20:
    shutil.rmtree(extract_dir3)

# Delete directory, where you unzip files
shutil.rmtree(extract_dir)
