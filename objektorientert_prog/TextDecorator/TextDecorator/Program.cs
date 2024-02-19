using Microsoft.VisualBasic;
using System;
using System.Diagnostics.Metrics;
using System.Diagnostics.Tracing;
using System.Runtime.InteropServices;
using System.Runtime.Serialization.Formatters;

namespace TextDecorator
{
    internal class Program
    {
        static char SymbolFinder(string text, char[] array1, char[] array2)
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
        static void Main(string[] args)
        {
            string[] arguments = Environment.GetCommandLineArgs();
            if (arguments.Length == 1)
            {
                Console.WriteLine("No arguments given! Try the help command!");
            }
            else if (arguments.Length == 2)
            {
                if (arguments[1].ToLower() == "help")
                {
                    Console.WriteLine($"Command syntax: <file> <Decorator> <Text>");
                }
                else
                {
                    Console.WriteLine("Too few arguments or unknown argument! Try the help command!");
                }
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

                else if (arguments[1].ToLower() == "alt") //alternative caps
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

                else if (arguments[1].ToLower() == "pig") //Pig latin
                {
                    char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };
                    char[] vowels = { 'a', 'e', 'i', 'o', 'u' };

                    string[] words = arguments[2].Split(' ');
                    foreach (string word in words)
                    {
                        if (vowels.Contains(Char.ToLower(word[0])))
                        {
                            Console.Write(word + "yay" + " ");
                        }
                        else if (consonants.Contains(Char.ToLower(word[0])))
                        {
                            List<char> startingLetters = new List<char>();

                            foreach (char letter in word)
                            {
                                if (vowels.Contains(Char.ToLower(letter)))
                                {
                                    break;
                                }

                                else if (consonants.Contains(Char.ToLower(letter)))
                                {
                                    startingLetters.Add(letter);
                                }
                            }

                            string strStartLetters = string.Join("", startingLetters);

                            if (Char.IsUpper(strStartLetters[0]))
                            {
                                string capitalizeWord = Char.ToUpper(word.Substring(startingLetters.Count)[0]) + word.Substring(startingLetters.Count + 1);
                                string uncapitalizeWord = Char.ToLower(strStartLetters[0]) + strStartLetters.Substring(1);
                                string completeWord = capitalizeWord + uncapitalizeWord;
                                char symbol = SymbolFinder(completeWord, vowels, consonants);

                                if (symbol == 'x')
                                {
                                    Console.Write(completeWord + "ay" + " ");
                                }
                                else
                                {
                                    string removedSymbol = completeWord.Remove(completeWord.IndexOf(symbol), 1);
                                    Console.Write(removedSymbol + "ay" + symbol + " ");
                                }
                            }
                            else
                            {
                                string firstHalf = word.Substring(startingLetters.Count);
                                string secondHalf = strStartLetters;
                                string completeWord = firstHalf + secondHalf;
                                char symbol = SymbolFinder(completeWord, vowels, consonants);

                                if (symbol == 'x')
                                {
                                    Console.Write(completeWord + "ay" + " ");
                                }
                                else
                                {
                                    string removedSymbol = completeWord.Remove(completeWord.IndexOf(symbol), 1);
                                    Console.Write(removedSymbol + "ay" + symbol + " ");
                                }
                            }
                        }
                    }
                }
                else if (arguments.Length == 3)
                {
                    Console.WriteLine("Unknown decorator used! Try the help command!");
                }
            }
        }

    }
}