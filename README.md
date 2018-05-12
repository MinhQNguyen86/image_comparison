## About
image_comparison looks through pairs of images and deletes duplicates.  
Outputs a csv file containing information about similarities between pairs.  
Requires a folder of images and a csv file containing the name of the images to be compared.
## Requirements & Installation
Python 3.4+ and pgmagick.
### Windows
Download an unofficial binary for pgmagick.
- [http://www.lfd.uci.edu/~gohlke/pythonlibs/#pgmagick](http://www.lfd.uci.edu/~gohlke/pythonlibs/#pgmagick)

Add Python's installation path to Window's Environment Variables.

- _Right click ***'My Computer' --> Properties --> Advanced system settings --> Environment Variables***_

- Create a new System Variable named `PYTHON_HOME` with value `C:\Python36` (Or whatever the installation path is for Python).

- Edit the System Variable PATH and add `;%PYTHON_HOME%\;%PYTHON_HOME%\Scripts\` to the end

Open cmd.exe as Administrator and type `pip install <whl file>`  
E.g. `pip install pgmagick-0.7.3-cp36-cp36m-win_amd64.whl`
### Linux
package install on Ubuntu:
```
Ubuntu11.10+
$ apt-get install python-pgmagick

Ubuntu10.04+
$ apt-get install libgraphicsmagick++1-dev
$ apt-get install libboost-python1.40-dev
```
package install on Fedora:
```
$ yum install GraphicsMagick-c++-devel
$ yum install boost-devel
```
GraphicsMagick from source package:
```
$ ./configure --enable-shared=yes
$ make && make install
```
**Install to:**
```
$ pip install pgmagick
```
### MacOSX
on MacOSX 10.11.6:
via homebrew and pip
```
$ brew install graphicsmagick
$ brew install boost-python --with-python3
$ pip install pgmagick
```
## Instructions

- Open cmd or terminal
### cmd
```
C:\WINDOWS\system32> python <location of image_comparison.py> <location of csv file> <location of image folder>
```
E.x.
```
C:\WINDOWS\system32> python "C:\Users\First Last\Desktop\img\image_comparison.py" "C:\Users\First Last\Desktop\imagetest.csv" "C:\Users\First Last\Desktop\images"
```
### Terminal
Make the script executable
```
$ chmod +x image_comparison.py
```
cd to the directory containing the program and then type
```
$ python3 image_comparison.py <location of csv file> <location of image folder>
```
E.x.
```
$ python3 image_comparison.py /Users/name/Documents/imagetest.csv /Users/name/Documents/images
```
### Note:
- The input csv file should be in the format: `abc.png,xyz.png`
- In Terminal, depending on the version of Python, use either `python` or `python3`
- Ubuntu may require it to be ran as `sudo`
- Terminal alternative `$ ./hello.py <location of csv file> <location of image folder>`

## Software Design
1. I drew out a rough table, writing out all the information that is given in one column and the required output (to-do list) in the other
2. After completely understanding the client's needs and requirements went off to do some research on how to approach the problem. I looked up both ImageMagick and GraphicsMagick to get a clearer understanding of the tools required to solve this issue. The general consensus was that GraphicsMagick provided faster run times, which was the main reason why I chose it.
3. The Python API for GraphicsMagick (pgmagick) doesn't have any documentation, so I looked through the C++ documentation for ImageMagick and GraphicsMagick (same documentation) and found some useful methods. `GraphicsMagick.Image().compare()`, `GraphicsMagick.Image().normalizedMeanError()` were helpful in determining similarities between images.
4. With the correct logic, I implemented the algorithm. After getting the code to work I planned out how to implement a simple command line interface in order to make running the script for a folder of images more user friendly.
5. With everything working I created my own folder and csv file to unit test the code. I used duplicate images, duplicate images with one being slightly altered, images that are completely different, images that are different sizes, similar images with different sizes, etc.
