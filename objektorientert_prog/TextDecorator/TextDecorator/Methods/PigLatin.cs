using Microsoft.VisualBasic;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using TextDecorator.Symbolfinder;

namespace TextDecorator.MethodPig
{
    public static class PigLatinClass
    {
        public static void PigLatinMode(string[] text)
        {
            char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
            char[] consonants = { 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z' };

            foreach (string word in text)
            {
                char firstLetter = char.ToLower(word[0]);

                if (vowels.Contains(firstLetter)) //Checks if firstletter is a vowel.
                {
                    char symbol = ListCompareClass.ListsComparison(word, vowels, consonants); //Returns symbol if exists.
                    if (symbol != '0')
                    {
                        string pigLatinNoSymbol = word.Remove(word.IndexOf(symbol), 1) + "yay"; //Finds the symbol and removes it from the string. 
                        Console.Write(pigLatinNoSymbol + symbol + " ");
                    }
                    else
                    {
                        Console.Write(word + "yay" + " ");
                    }
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

                        if (vowels.Contains(char.ToLower(letter))) //Goes out of loop if vowel.
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
                    char symbol = ListCompareClass.ListsComparison(word, vowels, consonants); //Returns symbol if exists.

                    if (upperCase) //If capitalized word
                    {
                        if (symbol != '0')
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
                        if (symbol != '0')
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
    }
}
