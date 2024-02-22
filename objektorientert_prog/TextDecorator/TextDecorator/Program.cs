using Microsoft.VisualBasic;
using System;
using System.Diagnostics.Metrics;
using System.Diagnostics.Tracing;
using System.Reflection.PortableExecutable;
using System.Runtime.InteropServices;
using System.Runtime.Serialization.Formatters;
using System.Security.Cryptography.X509Certificates;

namespace TextDecorator
{
    internal class Program
    {
        static char SymbolFinder(string text, char[] array1, char[] array2) //Compares to lists to find an element that isnt in either.
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
                    int counter = 0;

                    for (int i = 0; i < text.Length +2; i++) //+2 for the # to go over the text.
                    {
                        Console.Write("#");
                        if (i == text.Length +1 && counter == 0) 
                        {
                            Console.WriteLine($"\n#{text}#");
                            counter++; //Continue the loop for the floor of the box.
                            i = -1; //Sets to -1 to finish box
                        }
                    }
                }

                else if (decorator == "alt") //Alternating caps
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

                else if (decorator == "pig") //Pig latin
                {
                    char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };
                    char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
                    string[] wordArray = text.Split(' '); //Splits text string by blankspaces

                    foreach (string word in wordArray)
                    {
                        char firstLetter = char.ToLower(word[0]);

                        if (vowels.Contains(firstLetter)) //Checks if firstletter is a vowel.
                        {
                            Console.Write(word + "yay" + " "); 
                        }
                        else if (consonants.Contains(firstLetter)) //Check if firstletter is a consonant.
                        {
                            List<char> startingLetters = new List<char>();

                            bool upperCase = false;

                            foreach (char letter in word) //Checks for consonant clusters.
                            {
                                if (letter == 'y' && word.IndexOf(letter) == 1) //If y is in the second position it is counted as a vowel.
                                {
                                    break;
                                }

                                if (vowels.Contains(char.ToLower(letter))) //Go
                                {
                                    break;
                                }

                                else if (consonants.Contains(char.ToLower(letter)))
                                {
                                    if (char.IsUpper(letter))
                                    {
                                        upperCase = true; //Flags word, if it contains a capital letter.
                                    }
                                    startingLetters.Add(letter);
                                }

                            }

                            string strStartLetters = string.Join("", startingLetters); //Creates a string of the consonant cluster.
                            string pigLatinWord = word.Substring(strStartLetters.Length) + strStartLetters.ToLower() + "ay"; //Creates a string out of the cluster and rest of the word + ay
                            char symbol = SymbolFinder(word, vowels, consonants); //Returns symbol if exists.

                            if (upperCase) //If capitalized word
                            {
                                if (symbol != 'x')
                                {
                                    string pigLatinNoSymbol = pigLatinWord.Remove(pigLatinWord.IndexOf(symbol), 1); //Finds the symbol and removes it from the string. 
                                    Console.Write(char.ToUpper(pigLatinNoSymbol[0]) + pigLatinNoSymbol.Substring(1) + symbol + " "); //Capitalizes first letter and puts rest of word together with the symbol.
                                }
                                else
                                {
                                    Console.Write(char.ToUpper(pigLatinWord[0]) + pigLatinWord.Substring(1) + " "); //Does the same without symbol.

                                }
                            }
                            else //If uncapitalized word
                            {
                                if (symbol != 'x')
                                {
                                    string pigLatinNoSymbol = pigLatinWord.Remove(pigLatinWord.IndexOf(symbol), 1); //Finds the symbol and removes it from the string. 
                                    Console.Write(pigLatinNoSymbol + symbol + " "); //Writes the word with the symbol.
                                }
                                else
                                {
                                    Console.Write(pigLatinWord + " "); //If word is not capitalized or has symbol, prints word.
                                }
                            } 
                        }
                    }
                }
                else
                {
                    Console.WriteLine("Unknown decorator used! Try the help command!");
                }
            }
        }

    }
}