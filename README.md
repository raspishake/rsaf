# rsar - Raspberry Shake archive reader
conversion of archived miniSEED data to Raspberry Shake UDP-formatted ASCII, and forwarding of that data via UDP

rsar contains two tools:
- **packetize.py** - "packetize" data by converting from RS miniSEED into an ASCII file formatted in the style of RS UDP packets
- **run.py** - forward packetized RS data to a designated IP/port destination

## Installation



## Instructions



### packetize.py

Usage:

```bash
packetize.py -i infile.ms -o asciidata
```

### run.py
