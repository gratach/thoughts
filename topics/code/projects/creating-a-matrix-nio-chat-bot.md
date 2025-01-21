# Creating a matrix nio chat bot

A [matrix](../technologies/matrix-protocol.md) chat bot can be programmed with [matrix-nio](https://matrix-nio.readthedocs.io/en/latest/).

Examples for matrix chat bots can be found here:
[matrix-nio-basic-client](https://github.com/matrix-nio/matrix-nio/blob/main/examples/basic_client.py) (Basic not encrypted chat functionality)
[jeremiah-k-understanding-nio](https://github.com/jeremiah-k/understanding-nio/tree/master) (Encrypted chat bot template)

## End to end encryption

To enable end to end encryption for the matrix-nio chat bot the C library `libolm` has to be installed.
```
apt install libolm-dev
```
Matrix-nio has to be installed with the following option:
```
pip install matrix-nio[e2e]
```

When creating new chat bots that implement end to end encryption for a existing matrix user account they have to be verified by one of the other verified user devices (e.g. a element client) or else a warning message will be shown to a communication partners that has an encrypted chat conversation with the unverified chat bot.

Verification can be achieved by 

See also [matrix-nio-device-verification-bug](../bugs/matrix-nio-device-verification-bug.md)
