# rsaf - Raspberry Shake archive forwarder
conversion of archived miniSEED data to Raspberry Shake UDP-formatted ASCII, and forwarding of that data via UDP

rsar contains two tools:
- **packetize.py** - "packetize" data by converting from RS miniSEED into an ASCII (text) file formatted in the style of RS UDP packets
- **run.py** - forward packetized RS data to a designated IP/port destination

## Installation

This program is small but depends on other software. Installing rsudp will meet those dependencies.

Install [rsudp](https://github.com/raspishake/rsudp) for the operating system you're using (instructions are [here](https://raspishake.github.io/rsudp/installing.html)) prior to using this software.

## Instructions

1. In a terminal window, type the following to activate the rsudp environment:

    ```bash
    conda activate rsudp
    ```

2. Select a miniSEED file and convert it to ASCII text using the [``packetize.py`` script](#packetizepy).
3. Obtain the IP address and port of the computer you'd like to send packets to, then run the [main script](#runpy) on the ASCII text file 


### packetize.py

Usage:

```bash
packetize.py -i infile.ms -o asciidata
```

### run.py
