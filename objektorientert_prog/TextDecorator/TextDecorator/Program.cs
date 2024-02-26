using Microsoft.VisualBasic;
using System;
using TextDecorator.MethodAlt;
using TextDecorator.MethodBlock;
using TextDecorator.MethodPig;

namespace TextDecorator
{
    internal class Program
    {
        
        static void Main(string[] args)
        {
            string[] arguments = Environment.GetCommandLineArgs(); //Array with filepath and arguments if any.
            
            if (arguments.Length == 1)
            {
                Console.WriteLine("No arguments given! Try the help command!");
            }
            else if (arguments.Length == 2)
            {
                string decorator = arguments[1].ToLower();

                if (decorator.ToLower() == "help")
                {
                    Console.WriteLine($"Command syntax: <file> <Decorator> <Text>\nAvailable decorators: '#', 'alt', 'pig'");
                }
                else
                {
                    Console.WriteLine("Too few arguments! Try the help command!");
                }
            }
            else if (arguments.Length >= 3) 
            {
                string decorator = arguments[1].ToLower();
                string text = string.Join(" ", arguments.Skip(2)); //converts the arguments after the 2 first to a string.

                if (decorator == "#") //Block mode
                {
                    BlockMethodClass.BlockMode(text);
                }

                else if (decorator == "alt") //Alternating caps
                {
                    AlternatingCaseClass.AlternateCaseMode(text);
                }

                else if (decorator == "pig") //Pig latin
                {
                    string[] wordArray = text.Split(' '); //Splits text string by blankspaces

                    PigLatinClass.PigLatinMode(wordArray);

                }
                else
                {
                    Console.WriteLine("Unknown decorator used! Try the help command!");
                }
            }
        }

    }
}