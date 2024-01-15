namespace LuhnChecker;

class Program
{
    static void Main(string[] args)
    {
        string name = "Craig Marais";
        Console.WriteLine($"Luhn Checker by {name}");
        
        /*
         * Code me please...
         */
    }

    /// <summary>
    /// A method for checking a number using the Luhn Algorithm.
    /// </summary>
    /// <param name="num">The number to check.</param>
    /// <returns>(bool): True if the number is valid according to the Luhn algorithm, otherwise False.</returns>
    static bool Checker(int num)
    {
        // Take a given number, remove the last digit and then call Luhn()
        // If the number returned by Luhn() matches the removed item, then the number is valid.
        
        throw new Exception("Checker(): Not yet implemented yet.");
    }

    /// <summary>
    /// An implementation of the Luhn Algorithm.
    /// https://en.wikipedia.org/wiki/Luhn_algorithm
    /// </summary>
    /// <param name="num">The number to check.</param>
    /// <returns>(int): The check digit for the provided number.</returns>
    static int Luhn(int num)
    {
        // The Luhn algorithm should be implemented here
        
        throw new Exception("Luhn(): Not yet implemented.");
    }
}