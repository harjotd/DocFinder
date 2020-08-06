import re
import textract


class Document:
    '''
    This document class represents a single document that is passed in, and
    contains methods that takes the words from the documents and puts them
    into a list.
    '''
    def __init__(self, fname):
        self._word_dict = {}
        self._readable_text = self.docx_to_text(fname)
        self._file_length = 0
        for _word in self._readable_text:
            self._file_length += 1
            _word = _word.lower()
            _word = re.sub(r'\W+', '', _word)
            if _word not in self._word_dict:
                self._word_dict[_word] = 0
            self._word_dict[_word] += 1
        for _key in self._word_dict:
            self._word_dict[_key] = self._word_dict[_key] / self._file_length


    def docx_to_text(self, path):
        text = []
        try:
            text = textract.process(path, encoding='ascii')
            text = text.decode("utf-8")
            text = text.split()
        except:
            print("Couldn't open file" + path)
        return text


    def term_frequency(self, term):
        '''
        Takes a term as a parameter, and it will return the frequency of that
        term as appeared in the document that is being referred to. Will return
        0 if the word is not in the document.
        '''
        _term = term.lower()
        _term = re.sub(r'\W+', '', _term)
        if _term not in self._word_dict:
            return 0
        else:
            return self._word_dict[_term]

    def get_words(self):
        '''
        Returns all of the words in the document, no duplicate words.
        '''
        return list(self._word_dict.keys())
