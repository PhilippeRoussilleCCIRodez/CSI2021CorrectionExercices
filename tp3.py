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
        numbers = numbers.replace('\n', ',')
        number_list = numbers.split(",")
        for number in number_list:
            ret_value += int(number)
    return ret_value

add('''//M
1M2M3M5''')

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
        self.assertEqual(add("1\n2,3"), 6)
        self.assertEqual(add("3\n4\n5"), 12)


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
