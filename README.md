# prompt-charades-agentic-game
A game where player provides a brief description and generative AI model tries to guess the word.

This is my learning project to learn how to use generative AI Agents for building games. Source of my learning has been the course available on AnalyticsVidhya website as can be found here- https://courses.analyticsvidhya.com/courses/genai-to-build-exciting-games.

I have not used same concept as explained in the course using no-code platforms (e.g., replit or elevenlabs), but have taken my own approach in building similar game using a different tech-stack like python and flask (with mock demo version of gen ai model not using actual model). My aim is to only build my learnings here and not deploy an actual game/ app for public use.

## Introduction to the game
This game is more about how well a player creates the prompts and how well and quickly the generative AI model employed performs in guessing the word based on its understanding of the prompt. Short workflow is as below:
- Player enters their details and start playing the game.
- Timer for 90 seconds starts.
- Player is shown a word on screen (a word is selected randomply out of a list of words by the app without any repeats).
- Player crafts a prompt/description for the word shown and talks it through microphone.
- Web Speech API then converts the speech to text and sends it to the backend, which then passes it to a generative AI model.
- Generative AI model takes the prompt as input and comes up with a guess on what the word could be as quickly as possible and sends it back to backend. (Mock demo version of generative AI model response is used here for learning purpose).
- app scores the response and allots points for correct guesses, also keeps tracks of any incorrect guesses or if player has skipped the word and displays the current scores.
- At the end of 90 second timer app displays final results on the screen and gives option for Play Again.
