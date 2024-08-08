# Standard byte tree address

The standard byte tree address is a [[self-ending-data-format]] that describes a [[byte-tree-address]].

* If the byte tree address is `["+", []]` the byte sequence is `0xff 0xff 0xff'
* If the byte tree address is `["-", []]`the byte sequence is `0xff 0xff 0xfe`
* If the byte tree address is `["+", <sequece>]`with length(sequence) > 0 the byte sequence is `<sequence> 0xff`
* If the byte tree address is `["-", <sequence>]` with length(sequence) > 0 the byte sequence is  `0xff <sequence> 0xff`

#### Example:

* The byte tree address `["+", [1,2,3]]` is represented by the byte sequence `0x01 0x02 0x03 0xff`
* The byte tree address `["-", [4,5,6]]`is represented by the byte sequence `0xff 0x04 0x05 0x06`