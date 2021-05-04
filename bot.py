import os
import datetime
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

# set up the bot
bot = commands.Bot(
    irc_token=os.getenv('TMI_TOKEN'),
    client_id=os.getenv('CLIENT_ID'),
    nick=os.getenv('BOT_NICK'),
    prefix=os.getenv('BOT_PREFIX'),
    initial_channels=[os.getenv('CHANNEL')]
)

# Initialize play as True to indicate that the bot
# is able to send !play when a marbles is starting
play = True
play_count = 0
cooldown_timer_start = None


@bot.event
async def event_ready():
    print(f'Logged into Twitch | {bot.nick}')


# Activates on every message send in Twitch chat
@bot.event
async def event_message(ctx):
    global play, play_count, cooldown_timer_start, play_count_start

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    # If a message is "!play"
    if play and '!play' in ctx.content.lower():
        if play_count == 0:
            play_count_start = datetime.datetime.now()
            print("Counter is {} starting timer...".format(play_count))
        play_count += 1
        print("Counter is {}".format(play_count))
        # Counts until there has been 5 times !play in chat
        if play_count == 5:
            print("\nCounter is {}, time to play!".format(play_count))
            play_count_end = datetime.datetime.now()
            difference = (play_count_end - play_count_start)
            play_count_total_seconds = int(difference.total_seconds())
            print("{} times !play in the chat took {} seconds".format(play_count, play_count_total_seconds))
            # Only sends !play if the 5 !play messages were in a timespan of 20 seconds
            if play_count_total_seconds < 20:
                play = False
                play_count = 0
                cooldown_timer_start = datetime.datetime.now()
                print("\nSending !play... 150 second cooldown initiated")
                await ctx.channel.send("!play")
            else:
                print("{} times play not in the set timeframe, resetting counter...".format(play_count))
                play_count = 0

    if cooldown_timer_start is not None:
        cooldown_timer_end = datetime.datetime.now()
        difference = (cooldown_timer_end - cooldown_timer_start)
        total_seconds = int(difference.total_seconds())
        # Reactivates the ability to send !play in the chat
        # After the first !play has been send in the chat after 150 seconds
        if not play and total_seconds > 150:
            print("Set play to True, ready to send !play again")
            play = True


if __name__ == "__main__":
    bot.run()
