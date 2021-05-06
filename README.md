## Twitch chatbot for Marbles on Stream
### Does this ever happen to you?
_"Oh no I missed that my favorite streamer started their stream now i can't join in with Marbles!"_

### Well not anymore!
With this amazing chatbot you can always join in at a game of Marbles without having to miss a game! \
_Amazing, something you didn't know you desperately needed in your life._

### Preperation
But before you are able to always play Marbles, you have to do a few things:
1. If you don't have one already make a [Twitch](https://www.twitch.tv/) account, or just use the one you already have at the moment.
2. [Request an oauth code](https://twitchapps.com/tmi/). You need to login, so it can generate the code for you.
3. [Register an application](https://dev.twitch.tv/console/apps/create) and request a client-id, so you can interact with Twitch's API.
4. Don't forget to download [Python](https://www.python.org/downloads/) to be able to run the program!
5. Install the dependencies in requirements.txt with `pip install -r requirements.txt`.

### Configuring the bot
For the bot configuration you have to create and .env file in the directory of the project. \
Then you put in the following things:
```
TMI_TOKEN=oauth:
CLIENT_ID=
BOT_NICK=
BOT_PREFIX=!
CHANNEL=
```
`TMI_TOKEN` is the oauth token you generated beforehand. \
`CLIENT_ID` can be found on the application page after you registered one. \
`BOT_NICK` is the username of the account you logged into when registering your application. \
`BOT_PREFIX` is the prefix that is used when in future instances there will be commands added to this bot. \
`CHANNEL` is the channel that you want to connect to with the bot.

### Run the program
Now you're all set! \
The only thing you have to do is run the bot
```
python bot.py
```
