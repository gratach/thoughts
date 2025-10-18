## Distribution chain

When there are multiple members of a network which use different addresses to refer to different data blocks and the members can share the information which address belongs to which data block with each other, a distribution chain is the detailed history which members where involved in giving the information of a specific address, data block pair to a specific member.

## Example

If network member A created data block X with address x and member B copies it from A then the distribution history of (X,x) at B is A->B

When B gives the information about (X, x) to C the distribution history of (X,x) at C is A->B->C.

When C gets a conformation from A that the address x belongs indeed to the data block X then the distribution history of (X, x) at C is now {A->B-> | A->}C

## True distribution chain vs. passed on distribution chain

The true distribution chain is the real history of how the knowledge of the current data block was passed on to the current member. The passed on distribution chain is the knowledge of the distribution chain that the current member is aware of. This knowledge is passed on together with the data block content from each member of the distribution chain to the next one. 

## Dishonest network members

It is possible that some network members pass on false information about the data blocks or the distribution chain. Some other network member downstream in the distribution chain would now get false information about the distributed content. It is only possible to detect this false information if the betrayed network member has some different information by an other source. For example network member D might have to versions of data Blocks of address z: X and Y. X might have the passed on distribution chain A->B->D and Y might have the passed on distribution chain A->C->D. Member D can now decide on which version of data block he accepts based on whom he trusts more: B or C.
