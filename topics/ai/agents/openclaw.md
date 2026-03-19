# Openclaw

## Installation on server

Create a new debian server
[[configure-ssh-key-for-server]]
[[create-linux-user]] `<name_of_bot>` with sudo privileges.

Installation steps ([source](https://www.interserver.net/tips/kb/deploy-openclaw-self-hosted-ai-agent-ubuntu-guide/))

Install and update software
```
sudo apt update
sudo apt upgrade
sudo apt install git
sudo apt install polkitd
```

Install node + npm ([Instructions](https://nodejs.org/en/download))
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.4/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 24
```
Install openclaw
```
npm install -g openclaw@latest
```
Check version
```
`openclaw --version`
```


Onboarding
```
openclaw onboard --install-daemon
```

Make ssh tunnel to link localhost port 18789 of server and local machine

```
ssh -N -L 18789:127.0.0.1:18789 <name_of_bot>@<your_server_ip>
```

Start gateway

```
opneclaw gateway start
```

Open in browser

```
http://127.0.0.1:18789/#token=<insert_your_token>
```

The token can be found in `.openclaw/openclaw.json` 

## Setup matrix

==The setup of matrix was not jet successful.==

[source](https://docs.openclaw.ai/channels/matrix)

Install matrix bot sdk

```
npm install -g @vector-im/matrix-bot-sdk
```

Install matrix plugin

```
openclaw plugins install @openclaw/matrix
```

Create an matrix account.

Get an access token:

```
curl --request POST \
  --url https://matrix.org/_matrix/client/v3/login \
  --header 'Content-Type: application/json' \
  --data '{
  "type": "m.login.password",
  "identifier": {
    "type": "m.id.user",
    "user": "<your_user_name>"
  },
  "password": "<your_password>"
}'
```
If necessary replace `https://matrix.org` by your own matrix homserver url 


## Stop gateway

```
openclaw gateway stop
```
