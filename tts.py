from gtts import gTTS
import os
import pdf  # other file connect ho rha h 

def text_to_speech(text, output_file):
    tts = gTTS(text, lang="en")
    tts.save(output_file)

def main():
    pdf_path = "C:/Users/shrey/Downloads/SkillsBuild.pdf"
    extracted_text = pdf.extract_text_from_pdf(pdf_path)  # Actual extraction
    output_file = "output_audio.mp3"
    text_to_speech(extracted_text, output_file)
    
    os.system(f"start {output_file}")  # Playing the audio

if __name__ == "__main__":
    main()
