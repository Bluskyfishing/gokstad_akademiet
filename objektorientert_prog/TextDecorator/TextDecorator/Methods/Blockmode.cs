using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TextDecorator.MethodBlock
{
    public static class BlockMethodClass
    {
        public static void BlockMode(string text)
        {
            int counter = 0;

            for (int i = 0; i < text.Length + 2; i++) //+2 for the # to go over the text.
            {
                Console.Write("#");
                if (i == text.Length + 1 && counter == 0)
                {
                    Console.WriteLine($"\n#{text}#");
                    counter++; //Continue the loop for the floor of the box.
                    i = -1; //Sets to -1 to finish box
                }
            }
        }
    }
}
