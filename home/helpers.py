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

    total_sentences = len(probs)

    explicit_sentences = [w for w in probs if w > 0.975]
    # context_sentences = [w for w in probs if 0.80 < w < 0.975]
    # safe_sentences = [w for w in probs if w < 0.80]

    percentage = len(explicit_sentences) / total_sentences * 100
    rating = ""
    if percentage < 0.16:
        rating = "ALL"
    elif 0.16 < percentage < 0.40:
        rating = "PR"
    elif 0.40 < percentage < 0.60:
        rating = "R13"
    elif 0.60 < percentage < 0.80:
        rating = "RS"
    elif percentage > 0.80:
        rating = "RN"
    return percentage, rating


# G	ALL - All Readers - AR
# PG	PR - Parents and Readers - PR
# PG13	R13 - Readers Age 13 and up- R13
# R	RS - Restricted for Adult Only - RS
# NC17	RN - Not appropriate for Children - RN

if __name__ == "__main__":
    text = "what the fuck dude"
    text_list = text.split()

    print(probability(text_list))
