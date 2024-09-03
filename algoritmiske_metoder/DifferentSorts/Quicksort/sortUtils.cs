using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Quicksort
{
    internal class sortUtils
    {
        public static bool isSorted(int[] input)
        {
            for (int i = 0; i < input.Length; i++)
            {
                for (int j = i; j < input.Length - 1; j++)
                {
                    if (input[i] > input[j])
                    {
                        return false;
                    }
                }
            }
            return true;
        }
    }
}
