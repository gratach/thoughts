# Matrix nio no such room with id

Some strange bug occurs in [this script](https://github.com/gratach/test-matrix/blob/b446304f912375fc5c648147c6add7dbd02170fd/message_to_all_rooms.py) that implements a [matrix-nio-chat-bot](../projects/creating-a-matrix-nio-chat-bot.md) that sends messages to all joined rooms. A LocalProtocolError: "No such room with id ?" is raised in some cases when trying to send messages to the rooms.

The script lets the user choose on each execution if messages should be sent to all joined rooms or not. As long as the user chooses to send messages, everything works fine. When the user executes the script and chooses not to send messages, the error will appear in all following executions of the script. The error will disappear if anything gets written in the joined rooms and appear again if the script is executed without sending messages. The problem can be solved by adding the full_state=True parameter to the sync function.

[GitHub issue](https://github.com/matrix-nio/matrix-nio/issues/385)