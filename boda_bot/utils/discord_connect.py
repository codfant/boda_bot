import os
import discord
from dotenv import load_dotenv
from boda_bot.utils.cocktails import Cocktails
import re
from json.decoder import JSONDecodeError

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    help_messages = '''
$drink - Makes a random drink and shows the ingredients
$drink <drink name> - example $drink moscow mule
$ingredient <ingredient name> - example $ingredient Gin
    '''
    if message.content == '$help' or message.content == '$boda_bot':
        await message.channel.send(help_messages)

    if message.content == '$drink':
        ct = Cocktails()
        drink = ct.get_random_drink()
        await message.channel.send(drink)

    if re.search('\$drink\s[a-zA-Z\s]+', message.content):
        ct = Cocktails()
        try:
            drink = ct.get_drink_by_name(drink_name=str(message.content).split('$drink ')[1])
        except TypeError:
            drink = 'Drink Not Found!'
        await message.channel.send(drink)

    if re.search('\$ingredient\s[a-zA-Z\s]+', message.content):
        ct = Cocktails()
        ingredient_name = str(message.content).split('$ingredient ')[1]
        try:
            ingredient = ct.get_drink_by_ingredient(ingredient_name=ingredient_name)
        except JSONDecodeError:
            ingredient = 'No drinks found!'
        await message.channel.send(f'Drinks with {ingredient_name} in them:\r\n' + ingredient)


def run_it():
    client.run(TOKEN)


if '__main__' == __name__:
    run_it()
