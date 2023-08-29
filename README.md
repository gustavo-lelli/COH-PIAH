# COH-PIAH

This code is a simple implementation of a text analysis and classification system. It's designed to identify whether a given text is likely to be written by a student infected with a fictional condition called "COH-PIAH" based on linguistic features. The system uses a reference signature (a set of linguistic features) typical of a student with COH-PIAH, compares it with the signatures of input texts, and identifies which text is most similar to the reference signature.

Here's an overview of the major steps and components in the code:

Collecting Reference Signature:
The read_signature() function prompts the user to input values for linguistic features associated with a student infected with COH-PIAH. These features include the average word length, Type-Token ratio, Hapax Legomena ratio, average sentence length, average sentence complexity, and average phrase length. The function then returns these values as a list.

Collecting Texts:
The read_texts() function prompts the user to input multiple texts for analysis. These texts are read and stored in a list called texts.

Text Preprocessing:
There are several functions (separate_sentences(), separate_phrases(), separate_words()) that are responsible for breaking down the input texts into sentences, phrases, and words. These are crucial steps in analyzing the linguistic structure of the texts.

Calculating Signatures:
The calculate_signature() function takes a text as input and calculates its linguistic signature by computing various linguistic features. These features include the average word length, Type-Token ratio, Hapax Legomena ratio, average sentence length, average sentence complexity, and average phrase length. The calculated features are returned as a list.

Comparing Signatures:
The compare_signatures() function takes two signature lists as input and computes a similarity score between them. This score represents the difference between the features of two signatures. A lower similarity score indicates a higher similarity between the two signatures.

Evaluating Texts:
The evaluate_texts() function takes the list of input texts and the reference signature as inputs. It calculates the signature for each input text and compares each text's signature with the reference signature. The text with the most similar signature to the reference signature is considered the one most likely written by a student infected with COH-PIAH.

Outputting Results:
The code then calls the evaluate_texts() function, passing in the texts and the reference signature. It prints out which author (text) is most likely infected with COH-PIAH based on the linguistic analysis.