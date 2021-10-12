"""Module for exercise 3 in the third practical"""

__author__ = "Philippe ROUSSILLE"

import unittest
import random

def add(numbers : str) -> int:
    """This function adds numbers from a comma separated list and returns their sum."""
    ret_value = 0
    if numbers == '':
        ret_value = 0
    else:
        if numbers.startswith("//"):
            delimiter_list = []
            first_line, numbers = numbers.split('\n', 1)
            # first_line contient la première ligne
            # puis la suite
            # first_line est de la forme "//[CARACTERE]"
            # rappel : en Python, ça commence à 0
            delimiter_string = first_line[2:]
            delimiter_list.append(delimiter_string)
            # delimiter_string peut être de la forme "%.;/"
            # on va prendre chaque élément de delimiter_string
            # et l'ajouter à delimiter_list s'il n'y est pas déjà
            for element in delimiter_string:
                if element not in delimiter_list:
                    delimiter_list.append(element)
            for delimiter in delimiter_list:
                numbers = numbers.replace(delimiter, ",") #On remplace le caractère par une ","
        numbers = numbers.replace('\n', ',')
        number_list = numbers.split(",")
        negative_numbers = []
        exception_raised = False
        for number in number_list:
            num = int(number)
            if num < 0:
                negative_numbers.append(number)
                exception_raised = True
            elif num < 1000:
                ret_value += num
        if exception_raised:
            raise ValueError("negatives not allowed : " + ','.join(negative_numbers))
    return ret_value

class TestCalculatrice(unittest.TestCase):
    """Test class for add function."""
    def test_nul(self):
        """Checks against the empty string."""
        self.assertEqual(add(""), 0)

    def test_un_nombre(self):
        """Checks against one single number."""
        nbre = random.randint(0, 100)
        self.assertEqual(add(str(nbre)), nbre)

    def test_deux_nombres(self):
        """Checks against two numbers."""
        number1 = random.randint(0, 100)
        number2 = random.randint(0, 100)
        string = f"{number1},{number2}"
        #string = str(number1) + ',' + str(number2)
        self.assertEqual(add(string), number2 + number1)

    def test_nombres_quelconques(self):
        """Checks against an arbitrary number of numbers."""
        numbers = []
        chk_sum = 0
        for _ in range(random.randint(0, 100)):
            num = random.randint(0,100)
            numbers.append(str(num))
            chk_sum += num
        string = ','.join(numbers)
        self.assertEqual(add(string), chk_sum)

    def test_double_separateur(self):
        """Checks against a different separator (namely, a line break)."""
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("3\n4\n5"), 12)

    def test_autre_separateur(self):
        '''Checks against an arbitrary separator (specified in the first line of the input.
        First line begins with // and is optional.'''
        self.assertEqual(add("""//;\n1;2"""), 3)
        self.assertEqual(add("""//;\n1;2;3"""), 6)

    def test_nombres_superieur_mille(self):
        """Checks against numbers over 1000."""
        self.assertEqual(add("10001,10,111111"), 10)

    def test_nombres_negatifs(self):
        """Checks against negative numbers (an Exception should be raised)."""
        with self.assertRaises(ValueError):
            add("-1")

    def test_nombre_delimiteur_long(self):
        """Checks against a delimiter that has more than 1 character."""
        self.assertEqual(add("//:::\n1:::2:::3"), 6)

    def test_plusieurs_delimiteurs(self):
        """Checks against multiple delimiters."""
        self.assertEqual(add("//*%\n1*2%3"), 6)

# Test manuel de l'exception
#add("-1,-4,-4,0")

if __name__ == "__main__":
    unittest.main()

# Fonction split
# S'utilise sur les chaînes de caractères.
# "A,B,C,D".split(',') => ['A', 'B', 'C', 'D']
# liste = chaine.split(',')
# => Boucle for
# for element in liste:
# ... quelque chose avec element
# Convertir un str en int : nombre = int(chaine)

# Couper la chaîne [a:b] à b :
# chaine = chaine[b:]

# Indirection sur les listes/chaîne
# l est une liste/chaîne
# l[0] : premier élément
# l[1] : deuxième élément
# l[-1] : dernier élément
# l[-2] : avant-dernier élément
# Sous-liste/chaîne entre l'élément a et b
# l[0:1] : sous liste contenant les deux premiers éléments
# lorsque l'élément est non ambigü, il est optionnel
# par exemple
# l[0:1] == l[:1]
# l[1:-1] == l[1:]
