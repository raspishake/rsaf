# rsaf - Raspberry Shake archive forwarder
_conversion of archived miniSEED data to Raspberry Shake UDP-formatted ASCII, and forwarding of that data via UDP_

This software allows you to send archived Raspberry Shake data in UDP packets that are formatted identically to those sent by the Shake in real-time.

`rsaf` contains two tools:
- **packetize.py** - "packetize" data by converting from RS miniSEED into an ASCII (text) file formatted in the style of RS UDP packets
- **run.py** - forward packetized RS data to a designated IP/port destination

## Installation

This program is small but depends on other software. Installing [rsudp](https://github.com/raspishake/rsudp) will meet those dependencies.

1. Install [rsudp](https://github.com/raspishake/rsudp) for the operating system you're using (instructions are [here](https://raspishake.github.io/rsudp/installing.html)) prior to using this software.
2. In a new terminal window, type the following to activate the rsudp environment:

    ```bash
    conda activate rsudp
    ```

3. Install this software by doing the following (rsudp must be installed first):

    ```bash
    pip install rsaf
    ```

## Instructions to run

1. In a terminal window, type the following to activate the rsudp environment:

    ```bash
    conda activate rsudp
    ```

2. Select a miniSEED file (``infile.ms`` in this case) and convert it to ASCII text (``asciidata.txt``) using the [``packetize`` script](#packetize).

    ```bash
    packetize -i infile.ms -o asciidata.txt
    ```

3. Obtain the IP address and port of the computer you'd like to send packets to, then run the [main script](#run-rsaf) on the ASCII text file.

    ```bash
    rsaf -i asciidata.txt -d 192.168.1.110 -p 8888
    ```

## Brief documentation

### Packetize

This one-and-done script converts archived data from a Raspberry Shake (most commonly in miniSEED format) into Raspberry Shake UDP-formatted ASCII text and saves it in a text file. The input file must be valid seismic data from a Raspberry Shake, but it does not necessarily need to be in miniSEED format.

Usage:

```bash
packetize -i infile.ms -o asciidata.txt

Flags (all required):
[-i, --infile] input seismic data file
[-o, --outfile] output text file
```

### Run rsaf

To run rsaf, you'll need to know the destination computer's IP address. Most computers will show this in network settings. On linux, you can use the command ``hostname -I`` to do this without having to navigate a settings dialog.

_Note that some school networks will not allow this type of data transmission. This type of data transmission will also only work if you're on the same network as the destination computer, unless you have port forwarding configured in the receiving network's router._

Usage:

```bash
rsaf -i asciidata.txt -d 192.168.1.110 -p 8888

Flags (all required):
[-i, --infile] input text file
[-d, --dest] destination IP address (four 1-3 digit numbers separated by periods)
[-p, --port] destination port (a 1-5 digit number)
```

## rsudp

This software is a standalone adaptation of some tools found in [rsudp](https://github.com/raspishake/rsudp). Both are built by Ian Nesbitt, University of Maine.
