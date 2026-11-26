"""Illustrate the stages of a local voice assistant with sample text."""


def respond(transcript):
    """Return a predictable reply for a short demonstration transcript."""
    if not transcript.strip():
        return "No speech was captured. Try again."
    return f"Sample response to: {transcript.strip()}"


def main():
    print("JARVIS X voice flow demonstration")
    print("Capture -> transcription -> response -> playback")
    transcript = input("Enter a sample transcription: ")
    print(respond(transcript))
    print("Playback complete.")


if __name__ == "__main__":
    main()
