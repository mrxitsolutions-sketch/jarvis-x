# JARVIS X — Local Voice Assistant

**MRX IT SOLUTIONS** · AI & voice

A Windows voice assistant prototype with push-to-talk, local responses, and a stop control for playback. The working checkpoint brings speech input and response playback together in a browser interface.

Whisper transcribes a recording from the browser. Ollama streams the reply, and Windows speech synthesis turns it into audio that plays in the same browser.

## Explore

- [Open the interface demonstration](https://mrxitsolutions-sketch.github.io/mrx-website/demos.html#voice)
- [Read the project case study](jarvis-x-case-study.pdf)

## How the prototype works

1. A browser captures the user's push-to-talk recording.
2. Whisper transcribes the audio locally, with voice activity filtering.
3. Ollama streams the response text.
4. Windows speech synthesis produces audio for browser playback.

The project notes record a synthetic microphone test through transcription, response, and playback, plus backend and responsive-layout checks. The interface demonstration uses scripted prompts to illustrate the interaction.

## Try the Python example

```sh
python voice_flow_demo.py
```

The standard-library example illustrates the stages with sample text. The full voice prototype uses additional local components.
