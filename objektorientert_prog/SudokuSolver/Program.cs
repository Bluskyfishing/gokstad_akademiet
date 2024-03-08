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
            public bool SubBoxChecker(char[][] board, int start)
            {
                List<char[]> tempList = new List<char[]>();
                List<char[]> listbox = new List<char[]>();
                List<char> resultList = new List<char>();


                foreach (char[] row in board)
                {
                    tempList.Add(row.Take(start).ToArray());
                }

                for (int i = 0; i < tempList.Count; i++)
                {
                    listbox.Add(tempList[i]);
                    if (listbox.Count() == 3)
                    {
                        for (int j = 0; j < listbox.Count(); j++)
                        {
                            for (int k = 0; k < listbox[j].Count(); k++)
                            {
                                if (listbox[j][k] == '.') continue;
                                resultList.Add(listbox[j][k]);
                            } 
                        }
                        foreach (char row in resultList)
                        {
                            Console.WriteLine(row);
                        }
                        resultList.Clear();
                    } 
                }

                return true;
            }
            public bool IsValidSudoku(char[][] board)
            {
                for (int i = 0; i < board.Length; i++)
                {
                    List<char> listWithoutDuplicates = new List<char>();
                    List<char> listWithoutDuplicates2 = new List<char>();

                    for (int j = 0; j < board[i].Length; j++)
                    {

                        if (!listWithoutDuplicates.Contains(board[i][j])) //Checks row if duplicate.
                        {
                            if (board[i][j] != '.')
                            {
                                listWithoutDuplicates.Add(board[i][j]);
                            }
                            
                        }
                        else
                        {
                            return false;
                        }

                        if (!listWithoutDuplicates2.Contains(board[j][i])) //Checks column if duplicate.
                        {
                            if (board[j][i] != '.')
                            {
                                listWithoutDuplicates2.Add(board[j][i]);
                            }
                            
                        }
                        else
                        {
                            return false;
                        }


                    }
                }
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
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'],
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'],
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'],
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'],
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'],
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'],
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'],
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']];

            Solution  solution = new Solution();

            Console.WriteLine(solution.IsValidSudoku(board));
            Console.WriteLine(solution.IsValidSudoku(board2));

            solution.SubBoxChecker(board, 3);
        }
    }
}
