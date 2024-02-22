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
        }
    }
}