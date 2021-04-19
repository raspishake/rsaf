import os, sys
import getopt
from obspy import read
from datetime import timedelta

SMP = {
    0.01: 25,
    0.02: 50,
}

def packetize(inf, outf):
    '''
    Reads a seismic data file and converts it to ascii text.
    :param str inf: the input data file to convert
    :param str outf: where to write the output file
    '''
    if os.path.isfile(os.path.expanduser(inf)):
        stream = read(inf)
        try:
            samps = SMP[stream[0].stats.delta]
        except KeyError as e:
            raise KeyError('Sampling frequency of %s is not supported. Is this Raspberry Shake data?' % (e))
        n = 0
        time = stream[0].stats.starttime

        with open(outf, 'w') as f:
            for i in range(0, int(len(stream[0].data)/samps)):
                ptime = time + timedelta(seconds=stream[0].stats.delta*n)
                for t in stream:
                    data = ''
                    chan = t.stats.channel
                    for i in range(n, n+samps):
                        data += ', %s' % t.data[i]
                    line = "{'%s', %.3f%s}%s" % (chan, ptime.timestamp, data, os.linesep)
                    f.write(line)
                n += samps

            f.write('TERM%s' % (os.linesep))

        print('Data written to %s' % outf)
    else:
        print('Input file does not exist.')


def main():
    '''
    This function reads command line arguments, then calls
    :py:func:`rsar.packetize.packetize` with those arguments.
    '''

    hlp_txt='''
###########################################
##     R A S P B E R R Y  S H A K E      ##
##          Archive Packetizer           ##
##            by Ian Nesbitt             ##
##            GNU GPLv3 2021             ##
##                                       ##
## Convert archived Shake data from      ##
## from several common seismic formats   ##
## to RS UDP-packet-formatted ASCII.     ##
##                                       ##
##  Requires:                            ##
##  - obspy								 ##
##                                       ##
###########################################
Usage: python run.py -i FILE -d IP.ADR.OF.DST -p PORT
where := {
    -h | --help
            display this help message (optional)
    -i | --infile
            input seismic data file location
    -o | --outfile
            output text file location
    }
'''

    inf, outf = False, False
    opts = getopt.getopt(sys.argv[1:], 'hi:o:',
            ['help', 'in=', 'out=',]
            )[0]

    for opt, arg in opts:
        if opt in ('-h', '--help'):
            print(help_txt)
        if opt in ('-i', '--in='):
            inf = arg
        if opt in ('-o', '--out='):
            outf = arg
    if inf and outf:
        packetize(inf=inf, outf=outf)
    else:
        print(hlp_txt)

if __name__ == '__main__':
    main()
