# Introducing My Version of ZIP Bomb

## Introduction 
A zip bomb is a small zip file (a few MB in my case, but it could be smaller) that can potentially become petabytes (1 million GB), exabytes (1 billion GB), zettabytes (1 trillion GB), or more when extracted. This is quite dangerous for your devices as it can exhaust your CPU, RAM, and fill up your drive, oftentimes crashing and freezing your computer. 

The reason that a small zip file could expand to trillions of GBs is that zip removes redundancy effectively. Consider this: if I wrote ```0000000000000000...```, the compression algorithm will notice it is just a repeated string of "0", and so it will probably represent it in this form: ```1000 zeros```. This is, of course, an oversimplification, but you get the idea. If you dig very deep into the zip bomb, you will notice that it is just the same character repeated many times. This is because the same, repeated character has way more redundancy than unique ones. 

For example:\
```0000000000000000...``` --> 1000 ```0```\
```Qx^4kL@ap\0pE Qx^4kL@ap\0pE :`Q*_-].,1a```  --> 2 ```Qx^4kL@ap\0pE``` 1 ```:`Q*_-].,1a``` This is so much less efficient that just repeated strings

Since there's more redundancy, the compression ratio will be very high, at over 99%, leaving you with less than 1% of the original file size! Now imagine the zip is cloned many times and compressed again. The compression algorithm will also notice the redundancy (I mean this time it is the file that's repeating, not the characters) and removes them, therefore giving, yet again, a 99% compression ratio! Now imagine the same trick is used over and over again, getting over 99% compression ratio each time. After about 7 times, you will be left with 0.000000000001% of the total size!

Nowadays, your computer will usually not let your computer explode when extracting a zip bomb, as the nested zip files have to be manually extracted, which can take a long time. However, you can actually bypass that through the use of recursive extraction, though this is highly not recommended.

## Algorithm
This is my algorithm for my zip bomb, which could be found in ```zipofdeath.py```:
1. In a text file, "0" is written millions of times (I set it to 20 million). The goal here is to create as much redundancy as possible, so that when compressed, the file will be very small.
2. Cloned the text files many times (in my case, it's 100).
3. Compressed the text files into a zip. You will notice that the file size has reduced dramatically by more than 99%.
4. Clone the zip files many times (in my case, it's 100), then compress them. 
5. Repeat step 4 for a ```n```number of times (in my case, it is 6). The bigger the ```n```, the larger the zip bomb will be.

## How Big Can It Be?
I will use my example to show how big it can be when fully extracted. 
* A standard UTF-8 text file takes up 1 byte per character. If I wrote "0" 20 mil times, the text file is 20MB. 
* I cloned the text file 100 times, so the total size is now 2000MB, or 2GB. 
* Now repeat it six more times, each time cloning the already cloned files 100 times. So the total duplications of the text files is $100^{7}$, making the total file size 2 zettaabytes! For comparison, you will be contributing to about 1.1% of the Internet!

Original: 20 MB\
$1st$ iteration: 2 GB\
$2nd$ iteration: 200 GB\
$3rd$ iteration: 20 TB\
$4th$ iteration: 2 PB\
$5th$ iteration: 200 PB\
$6th$ iteration: 20 EB\
$7th$ iteration: 2 ZB\
$nth$ iteration: $20 \times100^{n}$ MB

## Create Your Own Zip Bomb
You can try creating your own zip bomb by following the steps below. Make sure you have Python installed (preferably Python 3) and an IDE (such as Visual Studio Code). 
1. Clone the repository
```
git clone https://github.com/j-shenng08/zipofdeath.git
```

2. Navigate into the project directory
```
cd zipofdeath
```

3. Run the Python script
```
python3 zipofdeath.py
```

You can play around with the numbers in the Python script. However, I highly advised setting the number of iterations too high, as it will take a very long time to execute, eat up your computer RAM and CPU power, causing your computer to freeze or crash. Furthermore, compression ratio will eventually hit near 0%, making the file size will be astronomically large (congratulations, you have bombed yourself). The recommended limits are mentioned in the script. 
