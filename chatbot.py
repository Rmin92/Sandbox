# Chat Bot

# Sentences we'll Respond with if the user greeted us

GREETING_KEYWORDS = ("hello", "hi", "greetings", "hey", "What's up", "yo",)

GREETING_RESPONSES = ("sup bro", "hey", "*nods*", "the sky... DUH",)

def check_for_greetings (sentence) :
    """if any of the words in the users's input was a greeting,  return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
