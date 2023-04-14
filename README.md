# buildhere

Quick and dirty script to automatically build C programs in Docker. Also consider using [Docker static.py](https://github.com/joshdabosh/static.py) to pull requireid libraries for the binary.

This is mainly intended for CTF pwn authors! And please don't allow untrusted input!! There are definitely injections here!!!

## Requirements
`python3 -m pip install docker`


## Usage
```
usage: buildhere.py [-h] [-o OUTFILE] [-p PACKAGES] [-dr] [-c COMMAND] imagetag file

positional arguments:
  imagetag              Docker image tag to build in
  file                  Source code file

options:
  -h, --help            show this help message and exit
  -o OUTFILE, --outfile OUTFILE
                        Build output file
  -p PACKAGES, --packages PACKAGES
                        Comma-separated additional packages to install
  -dr, --dont-remove    When set, don't remove build container
  -c COMMAND, --command COMMAND
                        Custom build command
```