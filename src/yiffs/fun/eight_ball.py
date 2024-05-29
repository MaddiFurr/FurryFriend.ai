import discord
from discord import app_commands as apc
from ...services.BotService import bot
from ...services.WebhookService import send_webhook_message
from ...services.LoggingService import log
import random


async def eight_ball(interaction: discord.Interaction, question: str):
        """Ask the Magic 8-Ball a question!"""
        # Convert the question to a seed for the random function
        random.seed(question + str(random.randint(0, 1000)))

        # List of generic 8-ball responses
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes - definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]

        # Select a random response
        response = random.choice(responses)
        
        # Create a Discord embed
        embed = discord.Embed(
            title="🎱 Your Magic 8-Ball Result 🎱",
            color=discord.Color.blue()
        )

        # Add fields for the question and answer
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="", value="", inline=False)
        embed.add_field(name="Question", value=question, inline=True)
        embed.add_field(name="Answer", value=response, inline=True)

        # Set the image of the embed
        embed.set_image(url="https://media.giphy.com/media/rufA4eAG74WgYIALHb/giphy.gif")

        # Send the embed
        await interaction.response.send_message(embed=embed)
        await log(None,f"{interaction.user.name} asked the Magic 8-Ball: {question} and got the response: {response}", "/fun 8ball", interaction.user, interaction.channel)