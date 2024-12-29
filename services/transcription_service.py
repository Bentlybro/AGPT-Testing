import whisper
import asyncio

class WhisperTranscriber:
    def __init__(self):
        self.model = whisper.load_model("base")
    
    async def transcribe(self, audio_path: str) -> str:
        try:
            # Run transcription in a separate thread to avoid blocking
            loop = asyncio.get_event_loop()
            result = await loop.run_in_executor(
                None, 
                self.model.transcribe, 
                audio_path
            )
            
            return result["text"]
            
        except Exception as e:
            raise Exception(f"Transcription failed: {str(e)}")