from document import Document
import os
import re
import math


class SearchEngine:
    '''
    This file is the SearchEngine, it will take in a directory, process it,
    then ask for a term. It will return the documents that the term appears
    in. The position of the document returned depends on the tf_idf number
    which is calculated. If any word (single term, or multi-term) does not
    appear in the documents of the given directory, it will return None.
    '''
    def __init__(self):
        self._user_name = os.getenv("USERNAME")
        self._dir = "C:\\Users\\" + self._user_name
        self._inverse_index = {}
        self._document_tracker = {}
        self._length = 0
        for (dirname, dirs, files) in os.walk(self._dir):
            for filename in files:
                if filename.endswith('docx'):
                    self._length += 1
                    _filepath_ = os.path.join(dirname, filename)
                    single_document = Document(_filepath_)
                    self._document_tracker[filename] = single_document
                    list_of_words = single_document.get_words()
                    for word in list_of_words:
                        if word not in self._inverse_index:
                            self._inverse_index[word] = [filename]
                        else:
                            self._inverse_index[word].append(filename)

    def _calculate_idf(self, term):
        '''
        Takes in a term as a parameter, and calculates the idf number which is
        one of the numbers used to rank the documents. It's the length of the
        directory divided by the number of documents the term appears in. If
        the term does not appear in the document, it returns 0.
        '''
        if term not in self._inverse_index.keys():
            return 0
        else:
            return math.log(self._length / len(self._inverse_index[term]))

    def search(self, term):
        """
        Takes in a term as a parameter, and looks for the given term in
        the documents (the documents contained in the given directory).
        If the any single word does not appear in any of the documents,
        it will return None.
        """
        _result = []
        _complete_result = []
        _all_relevant_documents = set()
        _word = term.split()
        _query = []
        for word in _word:
            _query.append(re.sub(r'\W+', '', word.lower()))
        for word in _query:
            if word in self._inverse_index.keys():
                for _file in self._inverse_index[word]:
                    _all_relevant_documents.add(_file)
        for _file in _all_relevant_documents:
            _document_link = self._document_tracker[_file]
            _tf_idf = 0
            for word in _query:
                _tf_idf += (_document_link.term_frequency(word) *
                            self._calculate_idf(word))
            _full_name = self._dir + "/" + _file
            _result.append((_tf_idf, _full_name))
        for document in sorted(_result, reverse=True):
            _complete_result.append(document[1])
        return _complete_result
