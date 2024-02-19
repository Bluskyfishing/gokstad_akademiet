﻿using System;
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
                            List<int> capitalLettersIndex = new List<int>();
                            List<string> pigLatinWords = new List<string>();

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
                            string strStartLetters = string.Join("", startingLetters); //trenger a capitalize må sjekke hvert ord om det er capitalized def keepcapital? og fikse "?"-tegn 

                            if (Char.IsUpper(strStartLetters[0]))
                            {
                                string capitalizeWord = Char.ToUpper(word.Substring(startingLetters.Count)[0]) + word.Substring(startingLetters.Count);
                                string uncapitaliceWord = Char.ToLower(strStartLetters[0]) + strStartLetters.Substring(1);
                                Console.Write(capitalizeWord + uncapitaliceWord + "ay" + " ");

                            }
                            else
                            {
                                Console.Write($"{word.Substring(startingLetters.Count)}{strStartLetters}" + "ay" + " ");
                            }
                        }
                    }
                }
            }
        }

    }
}