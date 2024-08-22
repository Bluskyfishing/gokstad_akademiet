using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace recursiveList;

public class Fibonacci
{
    public static void fib(int n1, int n2, int max)
    {
        if (n1 + n2 >= max) { return; }
        int nNext = n1 + n2;

        Console.WriteLine(nNext);
        fib(n2, nNext, max);
        return;
    }
}