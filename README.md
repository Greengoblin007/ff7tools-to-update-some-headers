# ff7tools-to-update-some-headers

As you may or may not know, Cebix forgot to include some useful tools in his files (https://github.com/cebix/ff7tools). To be more specific, they allow to decompress these files:

- WINDOW.BIN (several graphics, game font and VFW)

- OPENING.BIN (several logotypes and initial credits)

- STAFF2.BIN (ending credits)

- CO.BIN (Battle Square roulette images)

But they do not offer a tool to automatically update the headers once you recompress the files. I programmed some tools in Python 3 to get the job done. I also included scripts to allow the 4-byte alignment necessary in some PSX files.

Regards!
