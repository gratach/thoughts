# Openclaw

## Installation on server

Create a new debian server
[configure-ssh-key-for-server](../../code/server/configure-ssh-key-for-server.md)
[create-linux-user](../../linux/basics/create-linux-user.md) `<name_of_bot>` with sudo privileges:
```
adduser --disabled-password <your-bot-name>
usermod -aG sudo <your-bot-name>
visudo
```
Change line `%sudo    ALL=(ALL:ALL) ALL` to `%sudo   ALL=(ALL:ALL) NOPASSWD: ALL` and save.
```
su <your-bot-name> -
cd ~
```

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
Install openclaw ([source](https://docs.openclaw.ai/start/getting-started))
```
curl -fsSL https://openclaw.ai/install-cli.sh | bash
```
`echo 'alias openclaw="~/.openclaw/bin/openclaw"' >> ~/.bashrc`

Alternatively this also could work
```
npm install -g openclaw@latest
```
Check version
```
`openclaw --version`
```


## Onboarding
```
openclaw onboard --install-daemon
```
## Run tasks in the background

Taks can be run in the background with temux
```
sudo apt install tmux
```
Run a prompt in the background with
```
tmux new -s <name of your temux environment> <your prompt>
```
You can use a terminal like bash as `<your prompt>` for a terminal that runs in the background
Configure gateway environment

If you are in a temux environment you can return to the main environment without ending the task by typing
` Ctrl+B D `

Return to your temux environment with:
```
tmux attach -t <name of your temux environment>
```
As temux environment names you can choose `gate` for the gateway and `tui` for the terminal ui

## Start the gateway
```
export XDG_RUNTIME_DIR=/run/user/$(id -u)
mkdir -p $XDG_RUNTIME_DIR
```
Start gateway in the background using
```
openclaw gateway start
```

Run terminal chat:
```
openclaw tui
```
## Configure matrix

See [documentation](https://docs.openclaw.ai/channels/matrix)

Add to `.openclaw/openclaw.json`
```json
{
    "channels":{
        "matrix": {
            "enabled": true,
            "homeserver": "<the homeserver url of your bots matrix account like e.g. https://matrix.org>",
            "accessToken": "<your access token (obtain as described below)>",
            "deviceName": "<name of the device>",
            "encryption": true,
            "groupPolicy": "disabled",
            "dm": {
                "enabled": true
                "policy": "allowlist",
                "allowFrom": [
                    "<your matrix id>"
                ]
            }
        }
    },
    "commands": {
        "ownerAllowFrom": [
            "matrix:<your matrix id>"
        ]
    },
    "plugins": {
        "enties": {
            "matrix": {
                "enabled": true
            }
        }
    }
}
```

To obtain your access token run
```bash
curl --request POST \
  --url <the homeserver url of your bots matrix account like e.g. https://matrix.org>/_matrix/client/v3/login \
  --header 'Content-Type: application/json' \
  --data '{
  "type": "m.login.password",
  "identifier": {
    "type": "m.id.user",
    "user": "<user name of your bots matrix account>"
  },
  "password": "<password of your bots matrix account>"
}'
```


Verify matrix
```
openclaw matrix verify self
```
## Add alternative models

An alternative model provider that supports the OpenAI API can be configured by editing the `.openclaw/openclaw.json` file:
```JSON
{
    "agents":{
        "defaults": {
            "models": {
                "<name of provider>/<name of model>" : {
                    "alias": "<your prefered alias>"
                }
            },
            "model":{
                "primary": "<name of provider>/<name of model>"
            }
        }
    },
    "models": {
        "providers": {
            "<name of provider>": {
                "baseUrl": "<endpoint of the OpenAI API of the provider>",
                "apiKey": "<your api key>",
                "models":[
                    {
                        "id": "<id of the model>",
                        "name": "<name of the model>"
                    }
                ]
            }
        }
    }
}
```
For a provider like Clarifai the values could be the following
- `"<name of provider>" = "clarifai"` 
- `"<baseUrl>" = "https://api.clarifai.com/v2/ext/openai/v1"` 
- `"<id of the model>" = "Kimi-K2_6"`

## Disable heartbeat

To disable the heartbeat add to `.openclaw/openclaw.json`:
```json
{
    "agents": {
        "defaults": {
            "heartbeat": {
                "every": "0m"
            }
        }
    }
}    
```

```

## Open UI locally in browser (not tested)

Make ssh tunnel to link localhost port 18789 of server and local machine

run on your local machine
```
ssh -N -L 18789:127.0.0.1:18789 <name_of_bot>@<your_server_ip>
```

Open in browser

```
http://127.0.0.1:18789/#token=<insert_your_token>
```

The token can be found in `.openclaw/openclaw.json` 


## Security

[Security info](https://docs.openclaw.ai/gateway/security)
```
gateway.controlUi.allowInsecureAuth=false
```

## No longer used


```
npm install -g @vector-im/matrix-bot-sdk
```

```
openclaw plugins install @openclaw/matrix
```

