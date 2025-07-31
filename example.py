from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def load_faqs_from_file(filepath):
    faqs = {}
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            if ':' in line:
                vraag, antwoord = line.strip().split(':', 1)
                faqs[vraag.strip()] = antwoord.strip()
    return faqs

def main():
    faqs = load_faqs_from_file("faqs.txt") #make this file like this = example prompt:answer
    if not faqs:
        print("no options found.")
        return

    vragen = list(faqs.keys())
    vectorizer = TfidfVectorizer().fit(vragen)
    vraag_vectors = vectorizer.transform(vragen)

    print("Welcome to the ai.") #change this maybe
    while True:
        inp = input("you: ").strip()
        if inp.lower() in {"stop", "exit", "quit"}:
            print("Thank you for your time, bye!")
            break

        inp_vec = vectorizer.transform([inp])
        sim = cosine_similarity(inp_vec, vraag_vectors)
        idx = np.argmax(sim)
        score = sim[0, idx]

        if score > 0.3:
            print(faqs[vragen[idx]])
        else:
            print("Sorry, I do not understand that yet.")

if __name__ == "__main__":
    main()
