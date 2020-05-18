# RubeusToCcache
A small tool to convert Base64-encoded .kirbi tickets from Rubeus into .ccache files for Impacket

## Overview

This is a small tool to handle a common use case I run into often. Rubeus outputs TGTs in Base64-encoded .kirbi files,
whereas Impacket tools, like `wmiexec.py` or `smbexec.py` use the .ccache file format. The two formats are easily
converted between, thanks to Impacket and Zer1t0's [ticket_converter.py](https://github.com/Zer1t0/ticket_converter).
But I wanted to be able to use the Rubeus `/nowrap` option and send it right to a tool to get both .kirib and .ccache
files. Which is what this script does. Big thanks to Zer1t0 and the [Impacket](https://www.secureauth.com/labs/open-source-tools/impacket) project.

## Usage

```
╦═╗┬ ┬┌┐ ┌─┐┬ ┬┌─┐  ┌┬┐┌─┐  ╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐
╠╦╝│ │├┴┐├┤ │ │└─┐   │ │ │  ║  │  ├─┤│  ├─┤├┤
╩╚═└─┘└─┘└─┘└─┘└─┘   ┴ └─┘  ╚═╝└─┘┴ ┴└─┘┴ ┴└─┘
              By Solomon Sklash
          github.com/SolomonSklash
   Inspired by Zer1t0's ticket_converter.py

usage: rubeustoccache.py [-h] base64_input kirbi ccache

positional arguments:
  base64_input  The Base64-encoded .kirbi, sucha as from Rubeus.
  kirbi         The name of the output file for the decoded .kirbi file.
  ccache        The name of the output file for the ccache file.

optional arguments:
  -h, --help    show this help message and exit
```

## Dependencies and Installation

RubeusToCcache is written for Python 3, and requires the impacket and pyasn1 Python libraries.

Run either `pip3 install impacket pyasn1` or `pip3 install -r requirements.txt`

```
git clone https://github.com/SolomonSklash/RubeusToCcache
cd RubeusToCcache
pip3 install -r requirements.txt
```
