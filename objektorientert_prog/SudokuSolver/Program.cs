using System;
using System.Linq;
using System.Reflection;
using System.Runtime.InteropServices;
using static System.Runtime.InteropServices.JavaScript.JSType;
namespace SudokuValidator
{
    internal class Program
    {
        public class Solution
        {
            public bool SubBoxChecker(char[][] board)
            {
                List<char[]> tempList = new List<char[]>();
                List<char[]> listbox = new List<char[]>();
                List<char> resultList = new List<char>();

                for (int column = 0; column < 3; column++)
                {
                    foreach (char[] row in board)
                    {
                        if (column == 0)
                        {
                            tempList.Add(row.Take(3).ToArray());
                        }
                        else if (column == 1)
                        {
                            tempList.Add(row.Skip(3).Take(3).ToArray());

                        }
                        else if (column == 2)
                        {
                            tempList.Add(row.Skip(6).ToArray());
                        }

                    }

                    for (int i = 0; i < tempList.Count; i++)
                    {
                        listbox.Add(tempList[i]);

                        if (listbox.Count() == 3)
                        {
                            foreach (char[] boxLine in listbox)
                            {
                                foreach (char letter in boxLine)
                                {
                                    if (letter == '.') continue;
                                    resultList.Add(letter);
                                }
                            }

                            HashSet<char> resultSet = new HashSet<char>(resultList);

                            if (resultList.Count() != resultSet.Count())
                            {
                                Console.WriteLine($"Number in the same square!");
                                return false;
                            }

                            listbox.Clear();
                            resultList.Clear();
                        }
                    }
                }
                return true;
            }
            public bool IsValidSudoku(char[][] board)
            {
                for (int i = 0; i < board.Length; i++)
                {
                    List<char> noDuplicates = new List<char>();
                    List<char> noDuplicates2 = new List<char>();

                    for (int j = 0; j < board[i].Length; j++)
                    {

                        if (!noDuplicates.Contains(board[i][j])) //Checks row if duplicate.
                        {
                            if (board[i][j] != '.')
                            {
                                noDuplicates.Add(board[i][j]);
                            } 
                        }
                        else
                        {
                            Console.WriteLine("Number in row!");
                            return false;
                        }

                        if (!noDuplicates2.Contains(board[j][i])) //Checks column if duplicate.
                        {
                            if (board[j][i] != '.')
                            {
                                noDuplicates2.Add(board[j][i]);
                            }
                        }
                        else
                        {
                            Console.WriteLine("Number in column!");
                            return false;
                        }
                    }
                }

                if (!SubBoxChecker(board)) { return false; }

                return true;
            }
        }
        static void Main(string[] args)
        {
            char[][] board = 
                [['5', '3', '2', '.', '7', '.', '.', '.', '.'], //TRUE
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']];

            char[][] board2 =
                [['8', '3', '.', '.', '7', '.', '.', '.', '.'], //FALSE
                ['6', '2', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']];

            char[][] board3 =
                [['.', '3', '.', '.', '7', '.', '.', '.', '.'], //FALSE 3 added first square
                ['6', '.', '3', '1', '9', '5', '.', '.', '.'],
                ['1', '9', '.', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']];

            Solution  solution = new Solution();

            Console.WriteLine(solution.IsValidSudoku(board));
            Console.WriteLine(solution.IsValidSudoku(board2));
            Console.WriteLine(solution.IsValidSudoku(board3));
        }
    }
}