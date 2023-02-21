import openai

openai.api_key = "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"


def get_translation_and_example(words):
    joined = "/".join(words)
    prompt = f"""for every word/phrase in the following list (where every word/phrase are separated by '/') explain to me its meaning in english and give me a sentence with this word in english.
    your answer should contain 3 columns, every row should look like "word in english": "explanation in english": "sentence with this word in english". And it should not be anything else except
    the mentioned data. Don't add any words or translations etc from yourself. Here is a list:
    {joined}"""
    model_engine = "text-davinci-003"
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=3333,
        n=1,
        stop=None,
        temperature=0.5,
    )

    response = completion.choices[0].text
    return response
