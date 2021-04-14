import discord
import os
from random import randint

R = range(1, 11)

rolls = []

init = []

roll = ["roll","roll ", "/roll", "/roll ", "Roll", "Roll "]

roll10 = ["roll10", "roll 10", "/roll10", "/roll 10", "Roll10", "Roll 10"]

init0 = ["init", "init ", "/init", "/init ", "Init", "Init "]

#Add people in here
pessoas = []

iniciativa = []

init1 = {}

client = discord.Client()

for c in R:
	for a in range(0, len(roll)):
		#Rolls
		rolls.append(f"{roll[a]}{c}")
		#Init
		init.append(f"{init0[a]}{c}")

@client.event
async def on_ready():
	print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
	if message.author == client.user:
		return

	#Where the fun begines - Rolls(Anti-Karol, favor n mexer)
	if any(word in message.content for word in rolls):
		n = randint(1, 20)
		for c in R:
			if any(word in message.content for word in roll10): 
				c0 = 30
				if c0 > n:
					s = 'Failure'
				else:
					s = 'Success!'
				await message.channel.send(f'roll (difficulty 10) -> {n} ({s})')
				break
			c0 = c * 3
			for a in roll:
				if message.content.startswith(f"{a}{c}"):
					if c0 > n:
						s = 'Failure'
					else:
						s = 'Success!'
					await message.channel.send(f'roll (difficulty {c}) -> {n} ({s})')
					if n == 1:
								await message.channel.send('CRITICAL!!! ;(')
					elif n == 20:
						await message.channel.send('CRITICAL!!! :)')
					break
					
	if any(word in message.content for word in init):
		for a in init0:
			for c in R:
				if message.content.startswith(f"{a}{c}"):
					x = c * 3
					iniciativa.append(x)
					for c0 in range(0, len(pessoas)):
						iniciativa.append(randint(1, 20))
					iniciativa.sort(reverse=True)
					y = z = 0
					for i, v in enumerate(iniciativa):
						if v == x and y == i:
							init1["Adver"] = v
						else:
							init1[pessoas[y]] = v
							y += 1
					for k, v in init1.items():
						z += 1
						await message.channel.send(f'{z:>2}º{k:^9}-{v:>4}')
                    break


client.run(os.getenv('TOKEN'))