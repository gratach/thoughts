# Self ending data format

A self ending data format is some data, that can appear in a stream of bytes that indicates its one length. As long as the beginning within the byte sequence and also the format is known one can deduce the exact number of bytes that the data unit occupies.

An example is a c string, that is ended by the 0x00 byte. An other example is the [standard-byte-tree-address-format](standard-byte-tree-address-format.md)