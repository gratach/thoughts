# Matrix-nio device verification bug

A bug occurring during the development of [matrix-nio-chat-bot](../projects/creating-a-matrix-nio-chat-bot.md) key verification.

When trying to verify a key with [emoji verification](https://matrix.org/docs/older/e2ee-cross-signing/) using the method [described on the python nio GitHub page](https://github.com/matrix-nio/matrix-nio/blob/45af13b70cc60f4bf7be6cdfd5513b7730ec3108/examples/verify_with_emoji.py) the callback for the key verification is not fired. See [this discussion](https://github.com/matrix-nio/matrix-nio/issues/430).

The proposed solution is to use [this](https://github.com/wreald/matrix-nio/blob/5cb8e99965bcb622101b1d6ad6fa86f5a9debb9a/examples/verify_with_emoji.py) source code instead.