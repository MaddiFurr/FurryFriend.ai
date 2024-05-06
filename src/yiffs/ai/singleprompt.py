import discord
from discord import app_commands as apc
import asyncio
from ...services.BotService import bot
from ...services.PermissionChecker import permission_checker
from ...services.GeminiService import single

async def single_prompt(interaction: discord.Interaction, prompt: str):
    """Prompt the AI!"""
    # Defer the response
    await interaction.response.defer(ephemeral=False)

    AI_RESPONSE = await single(prompt)
    response_text = '## Prompt:\n> {}\n\n## Response:\n>>> {}\n\n*DISCLAIMER: AI does make mistakes. Please be sure to validate all responses*\n*RESPONSE LENGTH: {} Characters*'.format(prompt, AI_RESPONSE.text, str(len(AI_RESPONSE.text)))
    
    if len(response_text) <= 2000:
        # Edit the deferred response
        await interaction.edit_original_response(content=response_text)
    else:
        channel = interaction.channel
        # Send a follow-up message
        await interaction.followup.send('The response was too long to send in one message. Sending in multiple messages...')
        await asyncio.sleep(3)
        chunks = [">>> " + response_text[i:i+1995] for i in range(0, len(response_text), 1995)]
        for chunk in chunks:
            await asyncio.sleep(3)
            await channel.send(chunk)
    
    print("{} ({}) has prompted an AI call (The response was {} characters).\nPrompt: {}\nResponse: {}".format(interaction.user.name,interaction.user.id,str(len(response_text)),prompt,AI_RESPONSE.text))
    return