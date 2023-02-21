# Anki flashcards auto-creation
#### Video Demo: https://youtu.be/AUnOxV2zzAo
#### Description:
!It's mandatory to insert an API key into the openai.api_key = "" row in a file chatGPT.py. Also in a pdf_files you are gonna find a sample pdf file that depicts the recommended pdf file struct!
My project is a program that helps users to learn English words through various methods such as image, sound and text. The program uses various libraries including math, os, random, sys, and genanki.

The main function of the program takes two arguments as input, input_text and output_text. The input text is the source of English words(.PDF file) and the output text is a .txt file that contains the translated words, their meanings, and example sentences.

For the first run, execute project.py file without any command line arguments. It's gonna create all the required folders if needed. Then, execute project.py with exactly 2 command line arguments(full paths to your pdf and txt files). Then the program checks for the existence of the output text file. If the file exists, it reads the contents and stores the English words in a list. If the file does not exist, the program calls the pdf_to_txt function to convert the input text (which could be a PDF file) into a text file, and stores the words in a list. The program then checks if the w_m_s.txt file exists, which contains the words, their meanings, and sentences. If it does not exist, the program uses the get_translation_and_example function to translate the English words, get their meanings and example sentences and stores them in the w_m_s.txt file.

Next, the program creates several directories including apkg_files, images, pdf_files, sounds, sounds/meanings, sounds/words, sounds/sentences, and txt_files, if they do not already exist.

The program then splits the contents of the w_m_s.txt file into three columns - word, meaning, and sentence - and stores each word in a dictionary as an object with its corresponding meaning and sentence. These dictionaries are then stored in a list cards.

Finally, the program checks if the corresponding image, meaning, sentence, and word sound files exist for each word. If any of the files do not exist, the program adds the missing files to different lists missings_imgs, missings_m, missings_s, and missings_w, respectively.

In conclusion, this program provides a comprehensive solution for learning English words through different methods such as text, sound, and image. The program also allows users to correct and update the words, meanings, and sentences as needed, making it an efficient and flexible tool for language learning.

###### More on scripts:
* image_to_text

    This script is a program that converts PDF files to text files. It uses the PyPDF2 and pytesseract libraries to extract the text from a PDF file, clean the text, and write it to an output text file. The script has three main functions:

    pdf_to_text(file_path, output_path): This function opens the PDF file, reads the contents, and writes the text to the output file.

    clean_file(file_name, output_path): This function cleans the text file by removing unnecessary spaces and formatting.

    pdf_to_txt(input_file, output_file): This is the main function that calls the previous two functions to convert a PDF file to a text file. The final result is a list of words that were extracted from the PDF file.
---
* chatGPT

   This script uses the OpenAI API to get translations and examples for a list of words. The script starts by setting the API key for OpenAI. The function get_translation_and_example takes a list of words as input and creates a prompt in the form of a string that asks for the meaning, explanation and sentence for each word. This prompt is then passed to the OpenAI API's Completion.create method along with some parameters such as the engine to use, the maximum number of tokens, the number of responses to generate, and the temperature value which controls the creativity of the response. Finally, the response is returned as a string containing the explanations and sentences for the input words.
---
* get_image

    This script uses the selenium and PIL libraries to scrape images from the Freepik website. The script uses a webdriver to open a browser and perform actions on the website. The browser used in this script is Brave, and its binary location is specified in the options. The script takes two parameters - delay and max_images. The delay specifies the time to wait before clicking on the image thumbnail, and max_images is the maximum number of images to scrape. The script also takes a list of dictionaries, where each dictionary represents a query to the website and has a word (the search term) and an id (the identifier for the image file).

    The script iterates over the list of queries and navigates to the URL of the Freepik website, using the word as the search term. It then clicks on the image thumbnails and saves the images to the file system. Before saving the image, the script checks if the image's dimensions are larger than 390x260, and if they are, the image is resized to fit within those dimensions. The image is then saved to the file system in JPEG format, with the filename being the id.