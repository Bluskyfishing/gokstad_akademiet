using System.IO;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;
using System.Runtime.InteropServices;

namespace luhn
{
    class Readfile
    {
        static void Main(string[] args)
        {
            string line;
            try
            {
                StreamReader sr = new StreamReader("luhn_numbers.txt");
                line = sr.ReadLine();

                while (line != null)
                {
                    Console.WriteLine(line);
                    if (Checker(line))
                    {
                        Console.WriteLine("Valid!");
                    }
                    else
                    {
                        Console.WriteLine("Invalid!");
                    }
                    line = sr.ReadLine();
                }
                sr.Close();
                Console.ReadLine();
            }
            catch (Exception e)
            {
                Console.WriteLine("Exception", e.Message);
            }
        }
        static bool Checker(string cardNumber)
        {
            
            int lastDigit = int.Parse(cardNumber[^1].ToString());
            string payLoad = cardNumber.Remove(cardNumber.Length - 1);
            if ((Luhn(payLoad) + lastDigit) % 10 == 0)
            {
                return true;
            }
            else
            {
                return false;
            }
        } 
        static int Luhn(string cardNumber)
        {
            List<int> luhnNumbers = new List<int>();
            int index = 1;
            foreach (char strNum in cardNumber)
            {
                try
                {
                    int intValue = (int)char.GetNumericValue(strNum);
                    if (index % 2 != 0)
                    {
                        int result = intValue * 2;
                        if (result >= 10)
                        {
                            int a = result / 10;
                            int b = result % 10;
                            result = a + b;
                        }
                        luhnNumbers.Add(result);
                    }
                    else
                    {
                        luhnNumbers.Add(intValue);
                    }
                    index++;
                }
                catch (Exception e)
                {
                    Console.WriteLine("Exception", e.Message);
                }
            }
            return luhnNumbers.Sum();
        }
    }
}