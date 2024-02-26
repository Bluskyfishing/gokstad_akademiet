using System;

namespace typTest
{
    internal class Program
    {
        static void Main(string[] args)
        {
            String word = "Test";
            Console.WriteLine(Char.ToString(word[0]) + Char.ToString(word[1]));

            string input = "Coding is fun!";
            char[] delimiter = new char[] { ' ' };

            string[] output = input.Split(delimiter);
            foreach(string element in output)
            {
                Console.WriteLine(element);
            }

            string[] cars = { "Volvo", "BMW", "Ford", "Mazda" };
            string castedCars= string.Join(" ", cars.Skip(2));
            Console.WriteLine(castedCars);

            //Palindrome

            List<string> palindromes = new List<string>()
            {
                "lol",
                "Racecar",
                "Never odd or even"
            };


            foreach (string palindrome in palindromes)
            {
                Console.WriteLine($"{palindrome}");
                Console.WriteLine(ChecksIfPalindrome(palindrome));
            }

        }
        public static bool ChecksIfPalindrome(string input)
        {
            //lol
            string lowerInput = input.ToLower();
            Array arrayReverse = lowerInput.ToCharArray();
            Array.Reverse(arrayReverse);
            string reverseWord = arrayReverse.ToString();
            Console.WriteLine(reverseWord);

            if (lowerInput == reverseWord)
            {
                Console.WriteLine("It is a palindrome!");
                return true;
            }
            else
            {
                Console.WriteLine("It is NOT a Palindrome!");
                return false;
            }
        }
    }
}