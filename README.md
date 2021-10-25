# Boda Bot

A bot for Discord to search for coctails and provide other neat features.

##Credit to thecocktaildb.com

This wouldn't be possible without this API: https://www.thecocktaildb.com/api.php

##Sample Boda Bot Running
```buildoutcfg
Cody — Today at 12:59 PM
$drink

Boda Bot
BOT
 — Today at 12:59 PM
https://www.thecocktaildb.com/images/media/drink/vxtjbx1504817842.jpg
Space Odyssey

Ingredients:
1 shot Bacardi  - 151 proof rum
1 shot  - Malibu rum
1 shot  - Pineapple juice
Orange juice
Grenadine
Cherries

Instructions:
Fill glass with ice and add shots of Bacardi and Malibu. Add splash of pineapple juice and top with orange juice. Add grenadine for color and garnish with cherries.
```

```buildoutcfg
Cody — Today at 1:18 PM
$drink White Russian

Boda Bot
BOT
 — Today at 1:18 PM
https://www.thecocktaildb.com/images/media/drink/vsrupw1472405732.jpg
White Russian

Ingredients:
2 oz  - Vodka
1 oz  - Coffee liqueur
Light cream

Instructions:
Pour vodka and coffee liqueur over ice cubes in an old-fashioned glass. Fill with light cream and serve.
```

```buildoutcfg
Cody — Today at 2:01 PM
$ingredient Lime Juice

Boda Bot
BOT
 — Today at 2:01 PM
Drinks with Lime Juice in them:
Absolut limousine
Acapulco
Amaretto Rose
Autodafé
Bacardi Cocktail
Bee's Knees
Bloody Punch
Blue Margarita
Blueberry Mojito
Captain Kidd's Punch
Casa Blanca
Cosmopolitan
Duchamp's Punch
Frozen Daiquiri
Frozen Mint Daiquiri
Frozen Pineapple Daiquiri
Gimlet
Gin Swizzle
Imperial Cocktail
Kamikaze
Margarita
Michelada
Moscow Mule
Munich Mule
Pegu Club
Pure Passion
Strawberry Daiquiri
The Last Word
Tommy's Margarita
Winter Paloma
Winter Rita
```

## Env File

You have to make a .env file in the main directory with a variable called 'DISCORD_TOKEN' in it.

example:
```
touch .env
echo 'DISCORD_TOKEN' = "'ABC123'" > .env
```

##Example of How To Connect To a Discord Channel
https://realpython.com/how-to-make-a-discord-bot-python/
