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
                    int counter = 0;

                    for (int i = 0; i < arguments[2].Length +2; i++)
                    {
                        Console.Write("#");
                        if (i == arguments[2].Length +1 && counter == 0)
                        {
                            Console.WriteLine($"\n#{arguments[2]}#");
                            counter++;
                            i = -1;
                        }
                    }
                }
                if (arguments[1].ToLower() == "alt") //alternative caps
                {
                    int index = 1;
                    foreach (char letter in arguments[2]) 
                    {
                        if (letter == ' ')
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
                        else 
                        { 
                            Console.Write(letter); 
                        }
                    }

                }
                char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };
                char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

                if (arguments[1].ToLower() == "pig") //Pig latin
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
                                Console.Write(Char.ToString(word[0]) + Char.ToString(word[1]) + "ay" + " " );
                            }
                            else
                            {
                                foreach (char letter in word.Substring(1))
                                {
                                    Console.Write(letter);
                                }
                                Console.Write(Char.ToString(word[1]) + "ay" + " ");
                            }

                        }
                    }
                }
            }
        }

    }
}