from gtts import gTTS


def text_to_speech(data, type):
    language = "en"
    folder = ""
    match type:
        case "m":
            folder = "meanings"
        case "s":
            folder = "sentences"
        case "w":
            folder = "words"

    for piece in data:
        text_to_speech = piece["to_speech"]
        id = piece["id"]
        speech = gTTS(text=text_to_speech, lang=language, slow=False)
        speech.save(f"sounds/{folder}/{type}_{str(id)}.mp3")
