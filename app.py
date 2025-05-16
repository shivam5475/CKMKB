import streamlit as st
from deep_translator import GoogleTranslator
from gtts import gTTS
from pydub import AudioSegment
import os
import tempfile

# Initialize translator
translator = GoogleTranslator(source='auto', target='zh-CN')

# Streamlit app title
st.title("Text to Chinese Converter with Audio")

# Text input
input_text = st.text_area("Enter text (English or Hinglish):", height=150)

# Voice selection
voice_option = st.selectbox("Select voice:", ["Male", "Female"])

# Translate and generate audio button
if st.button("Convert to Chinese and Generate Audio"):
    if input_text.strip():
        try:
            # Translate to Chinese (Simplified)
            chinese_text = translator.translate(input_text)
            if not chinese_text:
                raise ValueError("Translation failed: No result returned")
            st.write("**Translated Chinese Text:**")
            st.write(chinese_text)

            # Generate temporary audio file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tmp_file:
                tts = gTTS(text=chinese_text, lang='zh-cn', slow=False)
                tts.save(tmp_file.name)

                # Load audio with pydub
                audio = AudioSegment.from_mp3(tmp_file.name)

                # Adjust pitch for male/female voice
                if voice_option == "Male":
                    # Lower pitch for male voice
                    octaves = -0.2
                else:
                    # Higher pitch for female voice
                    octaves = 0.2

                new_rate = int(audio.frame_rate * (2.0 ** octaves))
                audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_rate})
                audio = audio.set_frame_rate(44100)  # Normalize frame rate

                # Export modified audio
                output_audio = tmp_file.name.replace(".mp3", f"_{voice_option.lower()}.mp3")
                audio.export(output_audio, format="mp3")

                # Display audio player
                st.audio(output_audio, format="audio/mp3")

                # Clean up temporary files
                try:
                    os.remove(tmp_file.name)
                    os.remove(output_audio)
                except Exception as e:
                    st.warning(f"Warning: Could not clean up files: {str(e)}")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text to convert.")

# Footer
st.markdown("---")
st.write("Note: Voice options are approximated by pitch adjustment due to gTTS limitations.")