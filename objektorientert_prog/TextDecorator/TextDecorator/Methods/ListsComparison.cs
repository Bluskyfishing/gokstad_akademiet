using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace TextDecorator.Symbolfinder
{
    public static class ListCompareClass
    {
        public static char ListsComparison(string text, char[] array1, char[] array2) //Compares to lists to find an element that isnt in either.
        {
            foreach (char letter in text)
            {
                char lowerLetter = char.ToLower(letter);

                if (!array1.Contains(lowerLetter) && !array2.Contains(lowerLetter))
                {
                    return lowerLetter;
                }
            }
            return 'x';
        }
    }
}
