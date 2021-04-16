import discord
from discord.ext import commands
import random

# Documentation available @ https://github.com/ChrisSapp/SWIRLE

intents = discord.Intents(messages = True, guilds = True, reactions = True, members = True, presences = True)
client = commands.Bot(command_prefix = '.', intents = intents)
client.remove_command('help')

# On bot startup display that SWIRLE is active
@client.event
async def on_ready():
	print('SWIRLE is online.')

########################## COMMANDS ##############################

# Help Command

@client.command(pass_context=True)
async def help(ctx):

	help_text = 'SWIRLE is a Discord bot designed to test the implementation of encryption with the Discord API.'

	author = ctx.message.author
	member = author

	embed = discord.Embed(
		colour = discord.Colour.blue()
	)

	embed.set_author(name = "SWIRLE Help List")
	embed.add_field(name = 'Secure Working Interpreter Robot Leaving Encryption (SWIRLE)', value = help_text, inline = False)
	embed.add_field(name = 'Documentation:', value = '**[GitHub](https://github.com/ChrisSapp/SWIRLE)**')

	await member.send(author, embed=embed)

# Clear Command
@client.command()
async def clear(ctx, amount = 10):
	await ctx.channel.purge(limit = amount)

# Set Caesar Command

caesar_shift = 0

@client.command(pass_context = True)
async def set_caesar(ctx, arg):

	global caesar_shift 
	
	caesar_shift = int(arg)

	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.red()
	)

	embed.set_author(name = "Caesar")
	embed.add_field(name = 'Caesar Shift', value = 'The Caesar key has been set to ' + str(caesar_shift))

	await ctx.send(author, embed = embed)

# Set Affine Command

affine_key = 1

@client.command(pass_context = True)
async def set_affine(ctx, arg):

	global affine_key
	
	affine_key = int(arg)

	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.red()
	)

	embed.set_author(name = "Affine")
	embed.add_field(name = 'Affine Key', value = 'The Affine key has been set to ' + str(affine_key))

	await ctx.send(author, embed = embed)

########################### EVENTS ##############################

## OPTIONAL ##
# Display a notification whenever a member joins the server
@client.event
async def on_member_join(member):
	messages = ["Hello!", "How are you doing?", "Howdy!"]
	channel = member.guild.get_channel('General Channel ID')
	print(f'{member} has joined a server.')
	await channel.send(f'{member}: {random.choice(messages)}')

## OPTIONAL ##
# Display a notification whenever a member leaves the server
@client.event
async def on_member_remove(member):
	print(f'{member} has left a server.')

# This is the code to decipher based on first letter of each word and display output in deciphered_text
@client.event
async def on_message(message):
	# Create a variable to store deciphered text
	deciphered_text = ''
	channel_id = 'Deciphered_Text Channel ID Here'

	# To decrypt message based on first letter of each word
	if message.content[0:2] == '$N':
		 # If the author of the message is SWIRLE don't return any text
		if message.author == client.user:
			return

		else:
			# Add first letter from the first word to dechiphered_text
			deciphered_text += message.content[2]
			
			# Loop through the sentence and add first letter of each word to deciphered_text
			for x in range (2,len(message.content)):
				# If the current character in the sentence is a space, skip this characted and move to next word
				if message.content[x] == ' ':
					letter = message.content[x+1]
					deciphered_text += (letter)

			# Print the author of the message and the deciphered text in the command line output
			print(f'{message.author}: {deciphered_text}')
		
		# Print the message author and deciphered_text into corresponding channel
		channel = client.get_channel(channel_id)
		await channel.send(f'||{message.author}: {deciphered_text}||')
		# Delete any message that is decrypted and send to deciphered_text channel
		await message.channel.purge(limit = 1)



	# To decrypt message based on Caesar cipher
	elif message.content[0:2] == '$C':
		# If the author of the message is SWIRLE don't return any text
		if message.author == client.user:
			return

		else:
			# Loop through each character in the message in order to determine correct way to decrypt character
			for char in message.content[2:]:

				# If the char is a space, add to the deciphered text as is
				if char == ' ':
					deciphered_text += char

				# If the char is uppercase, apply the corresponding decryption and add to deciphered_text
				elif char.isupper():
					deciphered_text = deciphered_text + (chr((ord(char) + (26 - caesar_shift) - 65) % 26 + 65))

				# Else, apply the corresponding decryption and add to deciphered_text
				else:
					deciphered_text = deciphered_text + chr((ord(char) + (26 - caesar_shift) - 97) % 26 + 97)
			
		# Print the author of the message and the deciphered text in the command line output
			print(caesar_shift)
			print(f'{message.author}: {deciphered_text}')
		
		# Print the message author and deciphered_text into corresponding channel
		channel = client.get_channel(channel_id)
		await channel.send(f'||{message.author}: {deciphered_text}||')
		# Delete any message that is decrypted and send to deciphered_text channel
		await message.channel.purge(limit = 1)



	# To decrypt message based on Affine Cipher
	elif message.content[0:2] == '$A':
		# If the author of the message is SWIRLE don't return any text
		if message.author == client.user:
			return
		
		else:
			# Create a dictionary of matching encryption and decryption keys
			d = {
				1: 1,
				3: 9,
				5: 21,
				7: 15,
				9: 3
			}
			
			# Define a list to store decrypted index value
			deciphered_text_list = []

			# Define a string for the alphabet
			alphabet = 'abcdefghijklmnopqrstuvwxyz'
			check = ' '

			# Loop through each character in the message content from the 2nd index through the end of the message
			for char in message.content[2:]:
				char = char.lower()
				if char in alphabet:
					# Find the index of the current character corresponding to alphabet
					index = alphabet.index(char)
					# Use current index and apply decryption formula to add new character index value to deciphered_text_list
					deciphered_text_list.append(((index * d[int(affine_key)]) % 26))

				# Check to see if character is a space
				elif char in check:
					deciphered_text_list.append(' ')

			# Loop through each value in deciphered_text_list
			for index in deciphered_text_list:
				if index != ' ':
					deciphered_text += alphabet[index]
				# Take current value and add corresponding character from alphabet to deciphered_text
				else:
					deciphered_text += ' '
			
			#Print the author of the message and the deciphered text in the command line output
			print(f'{message.author}: {deciphered_text}')
			
		# Print the message author and deciphered_text into corresponding channel
		channel = client.get_channel(channel_id)
		await channel.send(f'||{message.author}: {deciphered_text}||')
		# Delete any message that is decrypted and send to deciphered_text channel
		await message.channel.purge(limit = 1)

	await client.process_commands(message)


# Command to run SWIRLE in your server, will need to replace string with your server ID
client.run('Insert BOT ID Here')
