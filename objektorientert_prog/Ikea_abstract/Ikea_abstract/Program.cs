using Ikea_abstract.Products;
using Ikea_abstract.Interfaces;
using System;
using Microsoft.VisualBasic;

namespace Ikea_abstract 
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Sofa sofa = new Sofa(100000, "10-D",
                "A very large blue sofa!", "Take out of box, screw together feet first, then sides.");
            Console.WriteLine(sofa.Price());
            Console.WriteLine(sofa.GetShelf());
            Console.WriteLine(sofa.Description());
            Console.WriteLine(sofa.Assemble());
            Console.WriteLine(sofa.LivingRoom());
        }
    }
}