using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace TextDecorator.MethodAlt
{
    internal class AlternatingCaseClass
    {
        public static void AlternateCaseMode(string text)
        {
            int index = 1;

            foreach (char letter in text)
            {
                if (letter == ' ') //Blankspace doesnt affect next upper/lower case. 
                    Console.Write(letter);
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