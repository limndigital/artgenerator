## Basic Art Generator
### by culla

### Installation
You will need to install python on your machine

[download python](https://www.python.org/downloads/)

FOR WINDOWS just use the executable

FOR linux based systems you should already have Python installed. I would assume Mac systems have it bundled too?

And install the dependencies Pillow, numpy and pandas

-pip install --upgrade Pillow numpy pandas

IN WINDOWS you may need to use "py -m" at the beginning

-py -m pip install --upgrade Pillow numpy pandas

OR alternatively you can just double click the py file itself that you want to use.

### Artwork
Once you have those installed, replace the art with your own. For now, to get a hang of it, leave the current naming convention.

MORE art for each layer - means more traits for the collection. I generally try to go for a miniumum of 25 layers for eyes,ears,mouths and noses in PFP collections. But it's entirely up to you. Currently This project is set up with 3 BG layers. A,B and C. A and B layers randomly rotate.

### Run it
Navigate the where the folder is on your machine in the terminal/cmd window
For example
- cd Documents/git/artgenerator/ 

Then run it

- python3 artgenerator.py
 
OR

- python artgenerator.py

### YOU CAN ADD LAYERS AND REMOVE LAYERS
Just be sure to remove or add what you are or not using.
USE artgenerator-five.py as a guy NOTICE THE LINES THAT HAVE BEEN REMOVED.


OR replace the the default with artgenerator-no.py for the non rotating layers

It will output the final images to the output directory.
