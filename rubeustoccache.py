#!/usr/bin/python3
#
# Author:
#    Solomon Sklash (https://github.com/SolomonSklash)
#    Heavily based on ticket_converter.py by Zer1t0 (https://github.com/Zer1t0)
#
# Description:
#    This script will convert the Base64 representation of .kirbi files into both a decoded
#    .kirbi and a .ccache file, as used by Impacket scripts.
#
# References:
#    https://github.com/Zer1t0/ticket_converter
#    https://tools.ietf.org/html/rfc4120
#    http://web.mit.edu/KERBEROS/krb5-devel/doc/formats/ccache_file_format.html
#    https://github.com/gentilkiwi/kekeo
#    https://github.com/rvazarkar/KrbCredExport
#
# Usage:
#    ./rubeustoccache.py BASE64_BLOB ticket.kirbi ticket.ccache
#
import sys
import base64
import argparse
from impacket.krb5.ccache import CCache


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('base64_input', help="The Base64-encoded .kirbi, sucha as from Rubeus.")
    parser.add_argument('kirbi', help="The name of the output file for the decoded .kirbi file.")
    parser.add_argument('ccache', help="The name of the output file for the ccache file.")
    return parser.parse_args()

def main():
    banner =  "╦═╗┬ ┬┌┐ ┌─┐┬ ┬┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐\n"
    banner += "╠╦╝│ │├┴┐├┤ │ │└─┐   │ │ │  ║  │  ├─┤│  ├─┤├┤ \n"
    banner += "╩╚═└─┘└─┘└─┘└─┘└─┘   ┴ └─┘  ╚═╝└─┘┴ ┴└─┘┴ ┴└─┘\n"
    banner += (" " * 14) + "By Solomon Sklash\n"
    banner += (" " * 10) + "github.com/SolomonSklash\n"
    banner += (" " * 2) + " Inspired by Zer1t0's ticket_converter.py\n"

    print(banner)

    args = parse_args()

    try:
        result = base64.b64decode(args.base64_input.encode('ascii'))
    except:
        print("[!] Failed to decode provided base64 string.")
        exit(1)
    try:
        with open(args.kirbi, 'wb') as kirbi_file:
            kirbi_file.write(result)
            kirbi_file.close()
            print("[*] Writing decoded .kirbi file to " + str(args.kirbi))
    except:
        print("[!] Failed to write ticket to temporary .kirbi file.")

    try:
        convert_kirbi_to_ccache(args.kirbi, args.ccache)
        print("[*] Writing converted .ccache file to " + str(args.ccache))
    except:
        print("[!] Failed to convert .kirbi file to .ccache file.")
    print("[*] All done! Don't forget to set your environment variable: export KRB5CCNAME=" + str(args.ccache))

def convert_kirbi_to_ccache(input_filename, output_filename):
    ccache = CCache.loadKirbiFile(input_filename)
    ccache.saveFile(output_filename)

def convert_ccache_to_kirbi(input_filename, output_filename):
    ccache = CCache.loadFile(input_filename)
    ccache.saveKirbiFile(output_filename)

if __name__ == '__main__':
    main()
