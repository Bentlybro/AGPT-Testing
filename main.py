import discord
from discord.ext import commands
from config.config import DISCORD_TOKEN
from services.youtube_service import YouTubeDownloader
from services.transcription_service import WhisperTranscriber
from utils.file_handler import cleanup_files

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

@bot.command(name='transcribe')
async def transcribe(ctx, url: str):
    try:
        # Send initial message
        await ctx.send("Starting transcription process...")
        
        # Download YouTube video
        downloader = YouTubeDownloader()
        audio_path = await downloader.download_audio(url)
        
        # Transcribe audio
        transcriber = WhisperTranscriber()
        await ctx.send("Audio downloaded, starting transcription...")
        
        transcript = await transcriber.transcribe(audio_path)
        
        # Send results in chunks if necessary
        if len(transcript) > 2000:
            chunks = [transcript[i:i+2000] for i in range(0, len(transcript), 2000)]
            for chunk in chunks:
                await ctx.send(chunk)
        else:
            await ctx.send(transcript)
            
        # Cleanup
        cleanup_files(audio_path)
        
    except Exception as e:
        await ctx.send(f"An error occurred: {str(e)}")

def run():
    bot.run(DISCORD_TOKEN)

if __name__ == "__main__":
    run()