import openai
openai.api_key = "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"


def chatGPT(que):
    completion = openai.Completion.create(
        engine="text-davinci-002",
        prompt=que,
        max_tokens=300,
        temperature=0.6,
    )
    # print(completion)
    # print(str(completion['choices'][0]['text']))
    return str(completion['choices'][0]['text'])
