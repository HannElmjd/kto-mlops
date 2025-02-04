import unittest

def count_long_names(first_names, threshold=7):
    """ Compte le nombre de prénoms ayant plus de 'threshold' 'seuil'lettres et affiche le résultat """
    count = len([name for name in first_names if len(name) > threshold])

    for name in first_names:
        if len(name) > threshold:
            comparison = "supérieur"
        else:
            comparison = "inférieur ou égal"
        print(name + " est un prénom avec un nombre de lettres " + comparison + " à " + str(threshold))
    return count

class TestCountLongNames(unittest.TestCase):
    def test_default_threshold(self):
        first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(count_long_names(first_names), 4)

    def test_custom_threshold(self):
        first_names = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(count_long_names(first_names, threshold=8), 2)

    def test_empty_list(self):
        self.assertEqual(count_long_names([]), 0)

if __name__ == '__main__':
    unittest.main()