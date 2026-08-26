class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        wordToSimilarWords = defaultdict(set)

        for word1, word2 in similarPairs:
            wordToSimilarWords[word1].add(word2)
            wordToSimilarWords[word2].add(word1)

        print(wordToSimilarWords)

        for word1, word2 in zip(sentence1, sentence2):
            if word1 == word2 or word1 in wordToSimilarWords[word2]:
                continue

            return False

        return True