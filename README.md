# old scripts #
Some old scripts from ~2012/2013 I collected here, that were previously stored in several different repositories.

scripts
=======

Shell-{Scripts,Bits,Pieces,Snippets}

 - colst - Print colorized hexcodes defined in st's config.h  
 - dwmstatus - mpd, loadavgs, volume, date
 - imgurp - Take a screenshot, upload it to imgur and output BBCode to stdout and XClipboard
 - intmux - Open program in tmux || st
 - makevid.sh - Create video from audio-file and image
 - rupd - Pull changes in all git/svn/hg/cvs repos in a directory
 - xsstoggle - Toggle X-Screensaver-State, requires [xssstate](tools.suckless.org/xssstate)  
 - yt - yt URL - see [http://surf.suckless.org/files/not_flash](http://surf.suckless.org/files/not_flash) for surf integration.

xsetroot_random
===============
usage: xsetroot_random.py [-h] [-f FILE] [-x]

Chooses a random X root-window bg color, either by name or hexcode. Requires
'xsetroot'.

<pre>

optional arguments:
  -h, --help            show this help message and exit
  -f FILE, --file FILE  read color names and/or hexcodes from FILE (format:
                        one string per line)
  -x, --hex             generate a random hexcode

</pre>

rippy
=====

rippy is a python script to rip and encode files from audio-cds, it also supports automatic tagging, using cddb. 
(See TODO for not yet implemented and planned features)

### Requirements ###
python obviously  
[python cddb library](http://cddb-py.sourceforge.net/CDDB-1.0 "Get it!")  
[python id3 library](http://id3-py.sourceforge.net/ "Get it!")  
cdparanoia  
lame and/or flac and/or oggenc  

### Usage ###

<pre>

usage: rippy [-h] [-d PATH] [-e ENCODER] [-q QUALITY] [-O OPTIONS] [-T NUMBERS]
             [-t NAME] [-o PATH] [-v]

Rip and encode files from an audio-cd

optional arguments:
  -h, --help            show this help message and exit
  -d PATH, --device PATH
                        PATH to the cdrom device to use; default: /dev/cdrom
  -e ENCODER, --encoder ENCODER
                        The encoder to use: lame (mp3), flac (flac), oggenc
                        (ogg); default: lame
  -q QUALITY, --quality QUALITY
                        allowed values: low, mid, high, best; default: high
  -O OPTIONS, --options OPTIONS
                        Encoder specific options, see the respective man
                        pages. Caution: Must be properly quoted as one string!
  -T NUMBER(S), --track NUMBER(S)
                        Track/s to rip from the cd. Use cdparanoia compatible
                        specification; default: all
  -t NAME, --title NAME
                        Name/Naming-scheme for the track/s. Available
                        variables: _a_ - Artist; _b_ - Album; _t_ - Track
                        Title; _n_ - Track Number; _y_- Year; default: _n_-_t_
  -o PATH, --output PATH
                        PATH to output the files to, missing directories will
                        be created. Available variables: _a_ - Artist; _b_ -
                        Album; _y_- Year; default: /home/user/_a_-_b_/
  -v, --version         show version and exit

Requires cdparanoia and an encoder to be installed.

</pre>  
  

### TODO ###
- option to send manual input to cddb  
- handle encodings better  
- change variable-pattern (maybe something like: %a)  
- test more  
- config file (?)  
  
### Version ###
0.1  05/27/12  
0.2  05/27/12 _tagging support; better encoder support; clean up; new name_    
0.2b 05/28/12 _no config-lib; more global vars; -v flag_  
0.3  06/12/12 _add manual tagging and no tagging; even more global vars; clean up better_    
0.3b 08/06/12 _fix missing extensions bug; fix some typos_

sicin
=====

usage: sicin.py [-h] <FILE>

Input handler for sic. (http://tools.suckless.org/sic)
It provides line editing and a history buffer.
The prompt shows the default channel/user.
An empty prompt means it's the host.
Usage example:
  $ tail -f FILE | sic
  $ sicin.py FILE
Quit with ':q'

positional arguments:
  <FILE>      File that is piped into sic.

optional arguments:
  -h, --help  show this help message and exit
