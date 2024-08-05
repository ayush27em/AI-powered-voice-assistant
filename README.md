
# AI Voice Assistant

This AI Voice Assistant, named Jarvis, is a voice-controlled virtual assistant designed to perform various tasks such as web browsing, playing music, fetching news, and interacting with OpenAI for general queries. It leverages several libraries and APIs to provide a seamless user experience.

## Features

- **Voice Recognition**: Listens for commands using Google's speech recognition.
- **Web Browsing**: Opens popular websites like Facebook, Google, and YouTube on command.
- **Music Playback**: Plays songs from a predefined music library.
- **News Fetching**: Retrieves and reads out the latest news headlines.
- **AI Interaction**: Uses OpenAI's API for handling general queries.
- **Voice Output**: Provides spoken feedback using Google Text-to-Speech (gTTS) and Pygame.

## Requirements

- Python 3.x
- SpeechRecognition
- PyAudio
- webbrowser
- pyttsx3
- requests
- gtts
- pygame
- openai
- google-generativeai

## Setup

1. Clone the repository:

    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. Install the required packages:

    ```bash
    pip install SpeechRecognition pyttsx3 requests openai gtts pygame google-generativeai
    ```

3. Obtain API keys:
   - **OpenAI**: Create an account on [OpenAI](https://www.openai.com/) and get an API key.
   - **Google Generative AI**: Get your API key from [Google Cloud Console](https://console.cloud.google.com/).
   - **NewsAPI**: Register on [NewsAPI](https://newsapi.org/) and get an API key.

4. Replace the placeholder API keys in the code with your actual keys:

    ```python
    genai.configure(api_key="your_google_genai_api_key")
    newsapi = "your_newsapi_key"
    client = OpenAI(api_key="your_openai_api_key")
    ```

## Usage

1. Run the script:

    ```bash
    python jarvis.py
    ```

2. Say "Jarvis" to wake up the assistant.
3. Give commands like:
   - "Open Facebook"
   - "Open Google"
   - "Open YouTube"
   - "Play [song_name]"
   - "News"
   - Any general query for AI processing

## Code Explanation

- **Speech Recognition**: Uses `speech_recognition` to listen for the wake word and commands.
- **Text-to-Speech**: Uses `pyttsx3` for initial speech and `gtts` with `pygame` for subsequent responses.
- **Web Browsing**: Utilizes `webbrowser` to open specified websites.
- **Music Playback**: Fetches song links from a predefined music library and opens them in a browser.
- **News Fetching**: Uses `requests` to fetch top headlines from NewsAPI and reads them out.
- **AI Processing**: Interacts with OpenAI and Google Generative AI to process and respond to general queries.

## Future Enhancements

- Add more commands and functionalities.
- Improve error handling and robustness.
- Integrate with more APIs for extended features.

## Contributing

Feel free to fork this project, make improvements, and submit pull requests. Your contributions are highly appreciated!

