from typing import List


class CountVectorizer:
    """
    Convert a list into a document-term matrix.
    """

    def __init__(self):
        """
        Init method.
        """
        self.feature_names = []

    def fit_transform(self, corpus: List[str]) -> List[list[int]]:
        """
        Takes corpus and returns a document-term matrix.
        """
        self.feature_names = []
        dictionary: dict = {}

        for proposals in corpus:
            for word in proposals.split():
                word = word.lower()
                if word not in dictionary:
                    dictionary[word] = len(dictionary)
                    self.feature_names.append(word)

        count_matrix = [[0] * len(dictionary) for _ in range(len(corpus))]

        for num_proposal, proposals in enumerate(corpus):
            for word in proposals.split():
                word = word.lower()
                if word in dictionary:
                    count_matrix[num_proposal][dictionary[word]] += 1

        return count_matrix

    def get_feature_names(self) -> List[str]:
        """
        Returns the list of feature names.
        Names are columns in the document-term matrix.
        """
        return self.feature_names


def check():
    """
    Check function
    """
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]

    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)
    print('Feature names:', end=' ')
    print(vectorizer.get_feature_names())
    print('Count matrix:', end=' ')
    print(count_matrix)


if __name__ == '__main__':
    check()
