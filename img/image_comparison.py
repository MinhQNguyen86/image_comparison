#!/usr/bin/env python
import pgmagick as mag
import os
import csv
import time
import sys

'''
A short script that reads a .csv file and a folder
of images in order to determine how similar two
pairs are.

A result.csv file is created in the same
folder as this file with the following header:
[image1, image2, similar, elapsed] => (str, str, float, float)
A similar and elapsed value of -1 will be assigned to
any invalid inputs (i.e. filename doesn't exist)

Perfect duplicates (i.e. similar == 0) will be have
one image deleted from the pair.
'''


def meanError(pic):
    '''(pgmagick.Image()) -> float
    Returns a floating value representing the normalized
    mean error per pixel of a color reduced image.
    This value is used to compute the similarities
    between two images.
    '''
    # From API: Print detailed information about the image
    # Required for Errors to be valid
    pic.verbose(True)
    # Reduce number of colors
    # Requires True parameter (measureError)
    # in order to calculate error values
    pic.quantize(True)
    return pic.normalizedMeanError()


def difference(img1, img2):
    '''(pgmagick.Image(), pgmagick.Image()) -> float
    Returns a float value corresponding to how
    similar two images are.
    0   => identical
    >0 => different
    Uses the normalized mean error per pixel of
    two images to determine similarity. Two identical
    images will have the same error value.
    REQ: img1, img2 have be existing valid images
    (e.g. PNG, GIF, JPG, etc.)
    '''
    # Get the normalizedMeanError
    # of both pictures
    value1 = meanError(img1)
    value2 = meanError(img2)

    # Returns true if both images are identical
    same = img1.compare(img2)

    # Initalize the value to be returned
    # 0 = identical images
    # >0 = different images
    if same:
        value = 0
    else:
        value = abs(value1-value2)*100000
    # Rounds to a value between [0, ~100]
    return round(value, 2)

# Stores the location of the CSV input file
cs = sys.argv[1].replace('\\', '\\\\')

# Stores the location of the image folder
folder = sys.argv[2].replace('\\', '\\\\') + '\\\\'

# Stores the location of this file
output = os.path.dirname(os.path.abspath(__file__))

# Initalize header for results
results = [["image1", "image2", "similar", "elapsed"]]

with open(cs) as file:
    reader = csv.reader(file)
    data = []
    # Reads each line into a list
    # [ [a,b], [c,d], ..]
    for r in reader:
        data.append(r)
    for d in data:
        # Checks if the file names are valid
        if '.' in d[0] and '.' in d[1]:
            try:
                # See if the images exist
                img1 = mag.Image(folder + d[0])
                img2 = mag.Image(folder + d[1])

                # Start the clock
                start_time = time.clock()

                # Get the similarity value
                diff = difference(img1, img2)

                # Remove any duplicates
                if diff == 0:
                    os.remove(folder + d[1])

                # End the clock
                end_time = round(time.clock() - start_time, 3)
                results.append([d[0], d[1], diff, end_time])
            except:
                results.append([d[0], d[1], -1, -1])

# Write results to file in the same folder as the program
with open(output + '\\result.csv', 'w') as file:
    for line in results:
        for i in range(len(line)):
            file.write(str(line[i]))
            # Add the comma between entries
            if i != len(line)-1:
                file.write(",")
        file.write('\n')

print("Program Finished")
