# -*- coding: utf-8 -*-
import argparse
import datetime
import numpy as np
import os
import sys
import subprocess
import gnssrefl.gps as g
import gnssrefl.nmea2snr as nmea

def main():
    """
    Documentation about the purpose of this code should be added here.
    It should clearly list the inputs to this code.
    And provide examples. 

    If using "myway" option, you are required to input the station latitude
    longitude, and ellipsoid height (params lat, lon, height). This option
    computes azimuth and elevation angles from SP3 files, whereas default behavior
    fits polynomials to the low precision NMEA records.


    """
    
    parser = argparse.ArgumentParser()
    parser.add_argument("station", help="station name", type=str)
    parser.add_argument("year", help="year", type=int)
    parser.add_argument("doy", help="start day of year", type=int)

    parser.add_argument("-snr", default='66', help="snr file ending, 99: 5-30 deg.; 66: < 30 deg.; 88: all data; 50: < 10 deg", type=str)
    parser.add_argument("-doy_end", default=None, help="end day of year", type=int)
    parser.add_argument("-year_end", default=None, help="end year", type=int)
    parser.add_argument("-overwrite", default=None, help="boolean", type=str)
    parser.add_argument("-dec", default=None, help="decimation, seconds", type=int)
    parser.add_argument("-lat", default=None, help="latitude, degrees", type=float)
    parser.add_argument("-lon", default=None, help="longitude, degrees", type=float)
    parser.add_argument("-height", default=None, help="ellipsoid height,m", type=float)
    parser.add_argument("-myway", default=None, help="boolean", type=str)

    args = parser.parse_args()

#make sure environment variables exist.  set to current directory if not
    g.check_environ_variables()


    station = args.station; 
    NS = len(station)
    if (NS != 4):
        print('Illegal input - Station name must have 4 characters. Exiting.')
        sys.exit()

    year = args.year
    if len(str(year)) != 4:
        print('Year must be four characters long. Exiting.', year)
        sys.exit()    

    isnr = args.snr
    isnr = int(isnr)

    doy= args.doy
    if args.doy_end == None:
        doy2 = doy
    else:
        doy2 = args.doy_end
        
    year1=year
    if args.year_end == None:
        year2 = year 
    else:
        year2 = args.year_end
    doy_list = list(range(doy, doy2+1))
    year_list = list(range(year1, year2+1))
    
    overwrite = False
    if (args.overwrite == 'True') or (args.overwrite == 'T'):
        overwrite = True

    dec = 1
    if (args.dec is not None):
        dec = args.dec
    myway = False
    if (args.myway is not None):
        myway = True

    # for now set to zero as Makan's code does not need LLH
    lat = 0; lon = 0; height = 0;
    if args.lat is not None:
        lat = args.lat
    if args.lon is not None:
        lon = args.lon
    if args.height is not None:
        height = args.height
    llh = [lat,lon,height]    
    nmea.run_nmea2snr(station, year_list, doy_list, isnr, overwrite,dec,llh,myway)

if __name__ == "__main__":
    main()
