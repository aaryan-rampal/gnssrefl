# -*- coding: utf-8 -*-
"""
installs non-python executables
"""
import argparse
import wget
import os
import subprocess
import sys

def download_chmod_move(url,savename,exedir):
    """
    inputs are url, filename and executable directory
    it should chmod g+rwx and  move to exe area
    """
    wget.download(url,savename)
    os.chmod(savename,0o777)
    subprocess.call(['mv', '-f',savename, exedir])
    print('\n Executable stored:', savename)

def main():
    """
    command line interface to install non-python executables, specifically
    CRX2RNX and gfzrnx.  I should add teqc ... sigh
    https://stackoverflow.com/questions/12791997/how-do-you-do-a-simple-chmod-x-from-within-python
    author: kristine larson

    note: this code used to try to download fortran exe but this is no longer necessary
    because we have the fortran code within gnssrefl
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("opsys", help="operating system (linux64 or macos)", type=str)
# optional arguments

    args = parser.parse_args()

    opsys = args.opsys
    exedir = os.environ['EXE']
    if not os.path.exists(exedir):
        print('You need to define the EXE environment variable. Exiting')
        sys.exit()
    else:
        print('Your executable environment area: ', exedir)


    # where the executable files are (currently) stored publicly
    sto = 'https://morefunwithgps.com/public_html/'

    if (opsys == 'linux64'):
        savename = 'CRX2RNX'
        url = sto + savename + '.' + opsys + '.e'
        download_chmod_move(url,savename,exedir)

        savename = 'gfzrnx'
        url = sto + 'gfzrnx.' + opsys + '.e'
        download_chmod_move(url,savename,exedir)

    elif (opsys == 'macos'):
        savename = 'CRX2RNX'
        url = sto + savename + '.' + opsys + '.e'
        download_chmod_move(url,savename,exedir)

        savename = 'teqc'
        # added 2021sep13
        url = 'https://www.unavco.org/software/data-processing/teqc/development/teqc_OSX_i5_gcc4.3d_64.zip'
        try:
            subprocess.call(['unzip', savename + '.zip' ])
            subprocess.call(['mv', '-f',savename, exedir])
            print('\n teqc executable stored:', savename)
        except:
            print('some kind of kerfuffle trying to install teqc')

        savename = 'gfzrnx'
        url = sto + 'gfzrnx.' + opsys + '.e'
        download_chmod_move(url,savename,exedir)

    else:
        print('We do not recognize your operating system input. Exiting.')
        sys.exit()


if __name__ == "__main__":
    main()
