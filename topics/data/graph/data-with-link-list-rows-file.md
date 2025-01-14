# Data with link list rows file

This is a file format to store parts or the entirety of a [dwll network](data-with-link-list-network.md). A file of this format has the ending `dwllr`.

The file consists of one or multiple node entries. Each node entry defines one of the nodes of the dwll network.

## Node entry format

A node entry starts with an ID string that can be used to identify the node. This string is terminated by a double new line `\n\n`. An ID string is a sequence of bytes that must not be empty and is not allowed to contain any `\n` characters.

It then continues with the ordered list of edges pointing to other nodes. This list is written as the list of the ID strings of the other nodes. The list entries are separated by single line breaks. The list as a whole is terminated by double line breaks.

The next paragraph contains the number bytes in the nodes bytes data written in decimal characters 0-9. This number is terminated by a double line break.

The last paragraph is the raw bytes data of the node. The raw bytes are terminated by four line breaks.

The next node entry (if present) starts directly after the four line breaks.

## Example

This is the same example that is also used in the [dwll network definition](data-with-link-list-network.md) and is explained there in detail.

```
ZENOEX

ZENOEX

6

String



UPJELG

ZENOEX

3

Int



VKEIGL

ZENOEX

8

Sentence



ECSLMD

ZENOEX

4

Here



QJWEOB

ZENOEX

3

are



DUFNUB

UPJELG

1

4



MRKLYT

ZENOEX

5

words



SINRUR

VKEIGL
ECSLMD
QJWEOB
DUFNUB
MRKLYT

17

Language: English




```