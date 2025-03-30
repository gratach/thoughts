# Mail account backup

Log into the mail account with thunderbird (imap)
Make sure that all content is downloaded to the computer (Download progress at the bottom of the Window)

Under Linux the mail data is saved at the path:
`~/.thunderbird/<some-numbers>.default-default/ImapMail/public.<url-of-mail-provider>`

Copy this folder to a backup location

For each mailbox directory the backup directory contains two files:

`<name-of-the-mailbox-directory>` <- a mbox file
`<name-of-the-mailbox-directory>.msf` <- a msf file

The mbox fail contains a list of all email contents including the appendices

To view the contents of a mbox file copy it to `~/.thunderbird/<some-numbers>.default-default/Mail/Local Folders/'. Open thunderbird and navigate to the local folders section in the mail account overview. Note that this approach is only possible if you have registered with some mail accout in thunderbird.


