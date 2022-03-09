import fitz


def pdf_to_string(file):
    with fitz.open(file) as doc:
        text = ""
        for page in doc:
            text += page.getText()

    return text


def remove_stopwords(text):
    import nltk
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    # nltk.download('stopwords')
    # nltk.download('punkt')

    stop_words = set(stopwords.words('english'))

    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w.lower() in stop_words]

    filtered_sentence = []

    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)

    return filtered_sentence


def probability(text_list):
    from profanity_check import predict, predict_prob
    probs = predict_prob(text_list)

    words = [w for w in probs if w > 0.75]
    return (len(words) / len(probs)) * 100
