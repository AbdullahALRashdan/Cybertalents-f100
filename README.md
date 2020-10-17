## Recursive extractor

Forked from [AbdullahALRashdan/Cybertalents-f100](https://github.com/AbdullahALRashdan/Cybertalents-f100).

This script only works with single files that have been compressed multiple times, **each time compressed as a single file.**\
**The script will end once multiple files were detected.**

#### Supported compressions: kbg, arj, ppmd, zip, rzip, gzip, bzip2, tar, cab, arc, xz, 7z, zoo, rar

1. Make sure to install required data compression tools:\
`sudo apt-get install ppmd kgb arj rzip bzip2 cabextract nomarch zoo`\
**Note**: You may need to install `ppmd` and `zoo` packages manually.

2. Download [extract.py](https://github.com/mohamedhaddi/recursive-extractor/blob/master/extract.py) to your directory of choice, then create a child directory (_e.g._: `extracted/`) and copy your archive file there with no other files.
```
.
├── extract.py
└── extracted/
    └── your_archive
```


3. Set the value of `path` in [extract.py](https://github.com/mohamedhaddi/recursive-extractor/blob/master/extract.py) to your new directory name (default is `path = "extracted"`).

4. Run `./extract.py`.
