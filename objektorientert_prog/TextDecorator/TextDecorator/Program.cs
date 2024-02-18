using System;
using System.Diagnostics.Tracing;

namespace TextDecorator
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string[] arguments = Environment.GetCommandLineArgs();
            if (arguments.Length == 1)
            {
                Console.WriteLine("No arguments given!");
            }
            else if (arguments.Length == 3) 
            {
                if (arguments[1] == "#") //block mode
                {
                    Console.WriteLine("#################");
                    Console.WriteLine($"#{arguments[2]}#");
                    Console.WriteLine("#################");
                }
                if (arguments[1].ToLower() == "alt") //alt mode
                {
                    int index = 1;
                    foreach (char letter in arguments[2]) //Noe rart Skal være: "ThIs Is A tEsT."
                    {
                        if (letter == ' ')
                            Console.Write(letter);
                        else if (index % 2 == 0)
                        {
                            Console.Write(char.ToLower(letter));
                            index++;
                        }
                        else if (index % 2 != 0) //Kan bare ha else bedre sånn?
                        {
                            Console.Write(char.ToUpper(letter));
                            index++;
                        }
                    }

                }
                char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };
                char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

                if (arguments[1].ToLower() == "pig")
                {
                    string[] words = arguments[2].ToLower().Split(' ');
                    foreach (string word in words)
                    {
                        if (vowels.Contains(word[0]))
                        {
                            Console.Write(word + "yay" + " ");
                        }
                        else if (consonants.Contains(word[0])) //må bli gjort bedre, kan være opp til 3 konnsonanter for loop? :)
                        {
                            if (consonants.Contains(word[1]))
                            {
                                foreach (char letter in word.Substring(2))
                                {
                                    Console.Write(letter);
                                }
                                Console.Write(word[0] + word[1] + "ay" + " " ); //Noe rart med at the er char + string?=
                            }
                            else
                            {
                                foreach (char letter in word.Substring(1))
                                {
                                    Console.Write(letter);
                                }
                                Console.Write(word[1] + "ay" + " ");
                            }
                        }

                    }
                }
            }
        }

    }
}