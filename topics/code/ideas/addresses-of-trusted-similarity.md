# Addresses of trusted similarity

Concept for a dynamic assignment of addresses to the members of a decentralized network in a way that the similarity of addresses provides information about how much two members of the network trust each other:

At the Beginning each member of the network has a randomly chosen unique address consisting of an array of bits. The length of the addresses bit array is the same for all members. It is the smallest possible length that enables giving all members an unique address.

There is a mechanism that once in a while selects a random network member and let it choose one bit of its address that gets flipped. If any of the other network members has the new address that gets created in this way the according bit of its address is also flipped in a way that both network members exchange their address. The network members choose the flipped bit in a way that their address becomes similar to the addresses of other network members that they trust and different to the addresses of network members that they distrust.

In this way the mutual trust of two members of the network can be identified by the similarity of their addresses.