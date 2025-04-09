# opus-bitrate-analyzer
A python script that analyzes the bitrate-time of audio files created with the libopus codec in .opus format. opus bitrate analyzer

----
test:

192kbps, vbr on, libopus codec, compression level 10 ( Applies compression according to the selected bitrate setting, determines the print strength. A value of 10 is HQ. There is no compression. Quality is at the highest value. A value of 0 is LQ. Compression is the highest value. Quality is the lowest (LQ). ) . 
Code to convert file to opus:

    ffmpeg -i input.ext -vn -c:a libopus -b:a 192k -vbr on -compression_level 10 output.opus

Example:

size of the opus file: 6.528KB

![Best_for_Last_192kbps-compress_level_10_bitrate](https://github.com/user-attachments/assets/5c68f41c-4cd9-4693-9d0b-3d344f2b2bb6)

-------
-------
192kbps, vbr on, libopus codec, compression level 0, LQ, max compression (Keeps the bitrate as close as possible to bitrate value.)

    ffmpeg -i input.ext -vn -c:a libopus -b:a 192k -vbr on -compression_level 00 output.opus   

Example:

size of the opus file: 5.953KB

![Best_for_Last _192kbps-compress_level_0_bitrate](https://github.com/user-attachments/assets/b6594a92-ad3c-498c-b957-ce7f7f019d8e)


--------
--------
With this software we can understand whether an opus file is compressed in high quality or low quality.
--------
If you examine the two graphs, the music file that is highly compressed with 0 has a bitrate very close to 192kbps. This indicates a high level of compression, low quality and low size. Also, since the bitrate axis of the graph is up to 320kbps, the perception may be perceived as a higher compression level. If the bitrate axis were plotted with a maximum level of 510kbps, it would look and be perceived as a curve above 192kbps. the perception is that it is of higher quality than it actually is.
Looking at the other graph, there is a very wide range of bitrate levels. Data was recorded up to 400kbps. This shows that the compression level is low and the quality is high. The reason why the file size is larger is because of the quality. 
(In the second graph, the maximum point of the bitrate axis level is 510kbps. To compare the two graphs in terms of perception, imagine that both graphs are 510kbps and think about the actual graph. This way you will understand and perceive that the first graph is much more compressed).

The video bitrate analyzer was created using a python script:
https://github.com/InB4DevOps/bitrate-viewer/blob/main/_bitrate_analyzer.py

Thanks to [@InB4DevOps](https://github.com/InB4DevOps) 

Development is accelerated with the help of DeepSeek R1 DeepThink.

First it analyzes the opus file and creates a .csv table data file with bitrate - time columns.

This file creates a bitrate-time graph and saves it in .svg format.

It also saves in .png format.

Generates detailed bitrate-time graph in .html format for interactive and detailed graphing.

Requirements:

    Python 3.6+
    pip install -r requirements.txt
    FFprobe in your PATH.

System requirements:

    ffmpeg>=4.0
    ffprobe>=4.0

ffmpeg for Windows 11:

    choco install ffmpeg


Usage:

    python opus_bitrate_analyzer.py <file_name>.opus

Do not use space characters or unrecognized characters in the file name.


Analysis file names:

It registers with the name

    <file_name>_bitrate.csv
    <file_name>_bitrate.png
    <file_name>_plot.svg
    <file_name>_interactive.html

 


