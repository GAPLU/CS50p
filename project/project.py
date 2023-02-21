import math
import os
import random
import sys
import re

import genanki
import PyPDF2

from chatGPT import get_translation_and_example
from get_image import get_images_from_google
from text_to_speech import text_to_speech


def main():
    directories = [
        "apkg_files",
        "images",
        "pdf_files",
        "sounds",
        "sounds/meanings",
        "sounds/words",
        "sounds/sentences",
        "txt_files",
    ]
    try:
        input_text = sys.argv[1]
        output_text = sys.argv[2]
    except IndexError:
        for directory in directories:
            if not os.path.exists(directory):
                os.makedirs(directory)
        sys.exit(
            "You should provide 2 command line arguments: pdf_files/name_of_pdf_file, txt_files/name_of_txt_file"
        )


    counter = 0
    cards = []
    words_list = []
    words_stacks = []
    pile_of_words = []

    if os.path.exists(output_text) and os.access(output_text, os.R_OK):
        with open(output_text) as f:
            for line in f:
                words_list.append(line.strip())
    else:
        words_list = pdf_to_txt(input_text, output_text)
        tmp_file = output_text.replace("txt_files/", "")
        sys.exit(
            f"Check the {tmp_file} file and correct it if needed (it should contain only one column of english words), and launch the code again"
        )

    if os.path.exists("txt_files/w_m_s.txt") and os.access(
        "txt_files/w_m_s.txt", os.R_OK
    ):
        with open("txt_files/w_m_s.txt", "r", encoding="utf-8") as f:
            for line in f:
                line = line.replace("Explanation on English:", "")
                pile_of_words.append(line.strip())

    else:
        iterations = int(math.floor(len(words_list) / 50))
        for i in range(iterations):
            words_stacks.append(words_list[i * 50 : (i + 1) * 50])
        words_stacks.append(words_list[iterations * 50 : len(words_list)])

        for words_stack in words_stacks:
            translated_words = get_translation_and_example(words_stack)
            translated_words = translated_words.split("\n")

            with open("txt_files/w_m_s.txt", "a", encoding="utf-8") as f:
                for row in translated_words:
                    if row.strip():
                        row = row.replace("Explanation on English:", "")
                        f.write(f"{row}\n")

        sys.exit(
            "Check the w_m_s.txt file and correct it if needed (it should contain three columns of : english words, meanings, sentences), and launch the code again"
        )

    for pile in pile_of_words:
        try:
            word, meaning, sentence = pile.split(":")
            if counter < len(pile_of_words):
                cards.append(
                    {
                        "word": word.strip().replace('"', ""),
                        "meaning": meaning.strip().replace('"', ""),
                        "sentence": sentence.strip().replace('"', ""),
                        "id": counter,
                    }
                )
                counter += 1
            else:
                break
        except ValueError:
            pass

    words = []
    meanings = []
    sentences = []

    for card in cards:
        words.append(card["word"])
        meanings.append(card["meaning"])
        sentences.append(card["sentence"])

    missings_imgs = []
    missings_m = []
    missings_s = []
    missings_w = []

    for card in cards:
        id = card["id"]
        img_id = f"images/{str(id)}.jpg"
        m_id = f"sounds/meanings/m_{str(id)}.mp3"
        s_id = f"sounds/sentences/s_{str(id)}.mp3"
        w_id = f"sounds/words/w_{str(id)}.mp3"

        if os.path.exists(img_id) == False and os.access(img_id, os.R_OK) == False:
            missings_imgs.append({"word": card["word"], "id": card["id"]})

        if os.path.exists(m_id) == False and os.access(m_id, os.R_OK) == False:
            missings_m.append({"to_speech": card["meaning"], "id": card["id"]})

        if os.path.exists(s_id) == False and os.access(s_id, os.R_OK) == False:
            missings_s.append({"to_speech": card["sentence"], "id": card["id"]})

        if os.path.exists(w_id) == False and os.access(w_id, os.R_OK) == False:
            missings_w.append({"to_speech": card["word"], "id": card["id"]})

    if len(missings_imgs) > 0:
        get_images_from_google(0, 1, missings_imgs)

    if len(missings_m) > 0:
        text_to_speech(missings_m, "m")

    if len(missings_s) > 0:
        text_to_speech(missings_s, "s")

    if len(missings_w) > 0:
        text_to_speech(missings_w, "w")

    model_id = random.randrange(1 << 30, 1 << 31)
    deck_id = random.randrange(1 << 30, 1 << 31)

    my_deck = genanki.Deck(deck_id, "Words List")
    media_files = []
    for _ in range(len(cards)):
        image = f"images/{_}.jpg"
        sound_s = f"sounds/sentences/s_{_}.mp3"
        sound_w = f"sounds/words/w_{_}.mp3"
        sound_m = f"sounds/meanings/m_{_}.mp3"
        media_files.append(image)
        media_files.append(sound_s)
        media_files.append(sound_w)
        media_files.append(sound_m)

    my_package = genanki.Package(my_deck)
    my_package.media_files = media_files

    with open("stylings/styling.css") as f:
        css = f.read()
    my_model = genanki.Model(
        model_id,
        "Simple Model",
        fields=[
            {"name": "Word"},
            {"name": "Image"},
            {"name": "Sound"},
            {"name": "Sound_Example"},
            {"name": "Sound_Meaning"},
            {"name": "Meaning"},
            {"name": "Example"},
        ],
        templates=[
            {
                "name": "Card 1",
                "qfmt": """<div id='rubric'>Essential Capitals</div>
                        <div style='font-family: Arial; font-size: 70px;color:#FF80DD;'>{{Word}}</div>
                        <hr>
                        {{Sound}}<hr>""",
                "afmt": """<div style='font-family: Arial; color:#FF80DD;'>{{Word}}</div>
                        <hr>
                        {{Image}}
                        <hr>
                        <div  style='font-family: Arial; color:#00aaaa; text-align:left;'>
                        Meaning: {{Meaning}}</div>
                        <hr>
                        <div  style='font-family: Arial; color:#9CFFFA; text-align:left;'>
                        &nbsp;→&nbsp;Example: {{Example}}</div>
                        <hr>
                        {{Sound_Meaning}}
                        [sound:_1sec.mp3]
                        {{Sound_Example}}""",
            },
        ],
        css=css,
    )
    for card in cards:
        img_path = f"{card['id']}.jpg"
        sound_s = f"s_{card['id']}.mp3"
        sound_w = f"w_{card['id']}.mp3"
        sound_m = f"m_{card['id']}.mp3"
        my_deck.add_note(
            genanki.Note(
                model=my_model,
                fields=[
                    card["word"],
                    f"<img src='{img_path}'>",
                    f"[sound:{sound_w}]",
                    f"[sound:{sound_s}]",
                    f"[sound:{sound_m}]",
                    card["meaning"],
                    card["sentence"],
                ],
            )
        )

    my_package.write_to_file(f"apkg_files/{random.randint(1 << 30, 1 << 31)}.apkg")


def pdf_to_text(file_path, output_path):
    pdf_file = open(file_path, "rb")
    pdf_reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for _ in range(len(pdf_reader.pages)):
        page_obj = pdf_reader.pages[_]
        text += page_obj.extract_text()

    with open(output_path, "w", encoding="utf-8") as output_file:
        output_file.write(text)
        return True


def clean_file(file_name, output_path):
    pattern = r"\s+\d+\."
    digit = r"\d"
    with open(file_name, "r") as f:
        lines = f.readlines()

    clean_lines = []
    for line in lines:
        line = line.strip()
        if line and line[0].isdigit():
            _, line = line.split(".", 1)
            line = line.strip()
            if line:
                if re.search(digit, line):
                    first, second = re.split(pattern, line)
                    if first and second:
                        first = first.replace("  ", " ")
                        first = first.replace(" -", "-")
                        second = second.replace("  ", " ")
                        second = second.replace(" -", "-")
                        clean_lines.append(first.strip())
                        clean_lines.append(second.strip())
                else:
                    line = line.replace("  ", " ")
                    line = line.replace(" -", "-")
                    clean_lines.append(line)
        elif line:
            try:
                clean_lines[-1] = clean_lines[-1] + " " + line
            except IndexError:
                pass

    with open(output_path, "w") as f:
        for line in clean_lines:
            f.write(f"{line}\n")
        return True


def pdf_to_txt(input_file, output_file):
    words_list = []
    pdf_to_text(input_file, output_file)
    clean_file(output_file, output_file)
    with open(output_file) as f:
        for line in f:
            words_list.append(line.strip())
    return words_list



if __name__ == "__main__":
    main()
