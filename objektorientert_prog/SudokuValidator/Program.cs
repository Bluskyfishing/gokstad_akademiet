using System;
using System.Linq;
using System.Reflection;

namespace SudokuValidator
{
    internal class Program
    {
        public class Solution
        {
            public bool SubBoxChecker(char[][] board)
            {
                List<char[]> tempList = new List<char[]>();
                List<char[]> listBox = new List<char[]>();
                List<char> resultList = new List<char>();

                for (int column = 0; column < 3; column++) //Splits lists up in 3. 
                {
                    foreach (char[] row in board) //checks each 3 squares going vertically.
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
                        listBox.Add(tempList[i]);

                        if (listBox.Count() == 3) //Checks the "Square" when 3 lists has been added.
                        {
                            foreach (char[] boxLine in listBox)
                            {
                                foreach (char letter in boxLine)
                                {
                                    if (letter == '.') continue;
                                    resultList.Add(letter); //list has only numbers. 
                                }
                            }

                            HashSet<char> resultSet = new HashSet<char>(resultList); //Is shorter if duplicates exists.

                            if (resultList.Count() != resultSet.Count()) //if duplicates returns false.
                            {
                                Console.WriteLine($"Number in the same square!");
                                return false;
                            }

                            listBox.Clear();
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
                    List<char> rows = new List<char>();
                    List<char> columns = new List<char>();

                    for (int j = 0; j < board[i].Length; j++)
                    {

                        if (!rows.Contains(board[i][j])) //Checks row if duplicate.
                        {
                            if (board[i][j] != '.')
                            {
                                rows.Add(board[i][j]);
                            } 
                        }
                        else
                        {
                            Console.WriteLine("Number in row!");
                            return false;
                        }

                        if (!columns.Contains(board[j][i])) //Checks column if duplicate.
                        {
                            if (board[j][i] != '.')
                            {
                                columns.Add(board[j][i]);
                            }
                        }
                        else
                        {
                            Console.WriteLine("Number in column!");
                            return false;
                        }
                    }
                }

                if (!SubBoxChecker(board)) { return false; } //Calls func to find if duplicates in 3x3 grid.

                return true;
            }
        }
        static void Main(string[] args)
        {
            char[][] board = 
                [['5', '3', '.', '.', '7', '.', '.', '.', '.'], //TRUE
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