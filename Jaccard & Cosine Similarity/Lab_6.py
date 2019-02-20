import re
import math

global corpus
corpus = []

d1 = "I am Sam."
d2 = "Sam I am."
d3 = "I do not like green eggs and ham."
d4 = "I do not like them, Sam I am."

final_d1 = re.findall(r'\b[a-z]{1,}\b', d1.lower())  # removed punctuation using regular expression
final_d2 = re.findall(r'\b[a-z]{1,}\b', d2.lower())  # removed punctuation using regular expression
final_d3 = re.findall(r'\b[a-z]{1,}\b', d3.lower())  # removed punctuation using regular expression
final_d4 = re.findall(r'\b[a-z]{1,}\b', d4.lower())  # removed punctuation using regular expression

document1 = set(final_d1)
document2 = set(final_d2)
document3 = set(final_d3)
document4 = set(final_d4)


def jaccard(documenta, documentb):
    intersection = documenta.intersection(documentb)
    union = documenta.union(documentb)
    return len(intersection) / (len(union))


corpus.append(d1)
corpus.append(d2)
corpus.append(d3)
corpus.append(d4)


def freq(term, document):
    return document.count(term)


def docfreq(term):
    doc_count = 0
    term_doc = 0
    for list in corpus:
        doc_count += 1
        if term in list:
            term_doc += 1
    idf = math.log2(doc_count / term_doc)
    return idf


def weight(term, document):
    tf = freq(term, document)
    idf = docfreq(term)
    return tf * idf


def cos_similarity(doc, query):
    numerator = 0
    weight_term_doc = 0
    weight_term_query = 0
    for term in doc:
        if term in query:
            numerator += weight(term, doc) * weight(term, query)
    for term in doc:
        weight_term_doc += pow(weight(term, doc), 2)
    for term in query:
        weight_term_query += pow(weight(term, query), 2)
    return numerator / (math.sqrt(weight_term_doc * weight_term_query))


print("---------------------Jaccard Similarity---------------------------------")
print("-------------------------Part A-----------------------------------------")
print("The jaccard similarity of d1 and d2 is", jaccard(document1, document2))
print("The jaccard similarity of d1 and d3 is", jaccard(document1, document3))
print("The jaccard similarity of d1 and d4 is", jaccard(document1, document4))
print("The jaccard similarity of d2 and d3 is", jaccard(document2, document3))
print("The jaccard similarity of d2 and d4 is", jaccard(document2, document4))
print("The jaccard similarity of d3 and d4 is", jaccard(document3, document4))

print("\n")

print("----------------------Cosine Similarity----------------------------------")
print("--------------------------Part B-----------------------------------------")
print("The cosine similarity of d1 and d2 is", cos_similarity(d1, d2))
print("The cosine similarity of d1 and d3 is", cos_similarity(d1, d3))
print("The cosine similarity of d1 and d4 is", cos_similarity(d1, d4))
print("The cosine similarity of d2 and d3 is", cos_similarity(d2, d3))
print("The cosine similarity of d2 and d4 is", cos_similarity(d2, d4))
print("The cosine similarity of d3 and d4 is", cos_similarity(d3, d4))
