using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;
using TextDecorator.Symbolfinder;
using static System.Runtime.InteropServices.JavaScript.JSType;

namespace TextDecorator.MethodAlt
{
    internal class AlternatingCaseClass
    {
        public static void AlternateCaseMode(string text)
        {
            int index = 1;
            char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
            char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };

            foreach (char letter in text)
            {
                char symbol = ListCompareClass.ListsComparison(text, vowels, consonants);

                if (letter == ' ' || letter == symbol) //Blankspace/symbols/numbers doesnt affect next upper/lower case. 
                {
                    Console.Write(letter);
                }
                else if (index % 2 == 0)
                {
                    Console.Write(char.ToLower(letter));
                    index++;
                }
                else if (index % 2 != 0)
                {
                    Console.Write(char.ToUpper(letter));
                    index++;
                }
                else //Prints if text is not a letter. 
                {
                    Console.Write(letter);
                }
            }
        }
    }
}