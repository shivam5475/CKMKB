# CKMKB -> Text to Chinese Converter Streamlit App

This Streamlit app converts English or Hinglish text to Chinese (Simplified) text and generates audio in Chinese with male or female voice options (approximated via pitch adjustment).

## Features
- Translates English/Hinglish to Chinese using `deep_translator`.
- Generates Chinese audio using `gTTS`.
- Simulates male/female voices by adjusting pitch with `pydub`.
- Runs in GitHub Codespaces or locally.

## Prerequisites
- A GitHub account with Codespaces access (free tier or paid).
- For local setup: Python 3.8+, FFmpeg, and Git.

## Running in GitHub Codespaces
1. **Open Codespaces**:
   - Click the "Code" button on the repository page.
   - Select "Codespaces" > "Create Codespaces on main".
   - Wait for the Codespace to initialize.

2. **Set Up Environment**:
   - Open the terminal (Ctrl+` or Terminal > New Terminal).
   - Make the setup script executable:
     ```bash
     chmod +x setup.sh
     ```
   - Run the setup script to install FFmpeg and dependencies:
     ```bash
     ./setup.sh
     ```

3. **Run the App**:
   - Start the Streamlit app:
     ```bash
     streamlit run app.py --server.address=0.0.0.0 --server.port=8501
     ```
   - Codespaces will provide a forwarded URL (e.g., `https://<your-codespace-name>-8501.app.github.dev`).
   - If the URL doesn’t appear, go to the "Ports" tab, set port `8501` to "Public," and copy the URL.

4. **Use the App**:
   - Open the URL in your browser.
   - Enter English or Hinglish text (e.g., "Hello" or "Namaste, kya haal hai?").
   - Select "Male" or "Female" voice.
   - Click "Convert to Chinese and Generate Audio" to see the translated text and play the audio.

5. **Save Changes to Repository**:
   - Check for modified files:
     ```bash
     git status
     ```
   - Stage changes:
     ```bash
     git add .
     ```
   - Commit changes:
     ```bash
     git commit -m "Update app files"
     ```
   - Push to GitHub:
     ```bash
     git push origin main
     ```
   - Verify changes on the GitHub repository page.

## Running Locally
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install FFmpeg**:
   - **Windows**: Download from [FFmpeg](https://ffmpeg.org/download.html) and add to PATH.
   - **macOS**: `brew install ffmpeg`
   - **Linux**: `sudo apt-get install ffmpeg`

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the App**:
   ```bash
   streamlit run app.py
   ```
   - Open `http://localhost:8501` in your browser.

## Files
- `app.py`: Main Streamlit app.
- `requirements.txt`: Python dependencies.
- `setup.sh`: Script to install FFmpeg and dependencies in Codespaces.
- `README.md`: This file.

## Notes
- **Voice Options**: Male/female voices are approximated using pitch adjustment due to `gTTS` limitations.
- **Hinglish**: The app handles mixed English/Hindi text via `deep_translator`’s `auto` detection.
- **Codespaces Access**: Only users with repository access can launch Codespaces. For public access, consider deploying to [Streamlit Community Cloud](https://streamlit.io/cloud).
- **Saving Changes**: Codespaces autosaves files locally, but you must commit and push to save to the GitHub repository.

## Troubleshooting
- **Port Issues**: Ensure port `8501` is public in the Codespaces "Ports" tab.
- **Dependency Errors**: Re-run `./setup.sh` if dependencies are missing.
- **Translation Errors**: Check internet connectivity, as `deep_translator` requires online access.
- **Git Errors**: Ensure you have write access to the repository and the correct branch (`main`).

For issues, open a GitHub issue or contact the repository owner.