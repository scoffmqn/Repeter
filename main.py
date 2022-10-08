import discord
import time

class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    if message.author.bot:
      if message.author.id == 1022997442813247508:
        lMess = len(message.content)
        if lMess > 50:
          time.sleep(10)
        elif lMess > 40:
          time.sleep(8.5)
        elif lMess > 30:
          time.sleep(7)
        elif lMess > 20:
          time.sleep(5.5)
        elif lMess > 10:
          time.sleep(4)
        else:
          time.sleep(2.5)
        await message.delete()
    else:
      auteur = ""
      if message.author.id == 911662487584247809:
            auteur = "Divine"
      elif message.author.id == 428205629279043584:
            auteur = "Tom"
      elif message.author.id == 707579481178636338:
            auteur = "Niels"
      
      nMess = auteur + ", " + message.content
            
      await message.channel.send(nMess, tts=True)


client = MyClient()

client.run("MTAyMjk5NzQ0MjgxMzI0NzUwOA.GQemKi.daO2q6xeQY9d7AZpLiy0yZWPiP4pPS-3Q3SCbY")