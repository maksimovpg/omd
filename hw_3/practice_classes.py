from math import log
from omd import CountVectorizer


class TfidfTransformer:
    def __init__(self):
        pass

    @staticmethod
    def tf_transform(count_matrix: list[list[int]]) -> list[list[float]]:
        """
        Calculates the matrix of term-frequency - tf
        """
        return [
            [round(el / sum(line), 3) for el in line] for line in count_matrix
        ]

    @staticmethod
    def idf_transform(count_matrix: list[list[int]]) -> list[float]:
        """
        Calculate inverse document-frequency - idf
        """
        idf_list = []
        for i in range(len(count_matrix[0])):
            idf_list.append(sum([1 if row[i] else 0 for row in count_matrix]))

        idf: list[float] = []
        for el in idf_list:
            idf.append(round(log((len(count_matrix) + 1) / (el + 1)), 1) + 1)
        return idf

    def fit_transform(self, count_matrix: list) -> list[list[float]]:
        """
        Calculate tf x idf matrix
        """
        tf_matrix = self.tf_transform(count_matrix)
        idf = self.idf_transform(count_matrix)
        result: list[list[float]] = []
        for row in tf_matrix:
            result.append([round(a * b, 3) for a, b in zip(row, idf)])
        return result


class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tf_idf_transformer = TfidfTransformer()

    def fit_transform(self, corpus: list[str]) -> list[list]:
        """
        Transform the text into a feature matrix using CountVectorizer.
        Get tf x idf matrix using TfidfTransformer.
        """
        count_matrix = super().fit_transform(corpus)
        return self.tf_idf_transformer.fit_transform(count_matrix)


def check():
    """
    Check function
    """
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)
    print(vectorizer.get_feature_names())
    print(tfidf_matrix)


if __name__ == '__main__':
    check()
