using System;
using System.Linq;
using System.Runtime.InteropServices;
using static System.Runtime.InteropServices.JavaScript.JSType;
namespace SudokuSolver
{
    internal class Program
    {
        public class Solution
        {
            public bool IsValidSudoku(char[][] board)
            {
                for (int i = 0; i < board.Length; i++)
                {
                    List<char> listWithoutDuplicates = new List<char>();
                    
                    for (int j = 0; j < board[i].Length; j++)
                    {
                        Console.WriteLine("column");
                        Console.WriteLine(board[j][i]);
                        if (board[i][j] == '.') continue; 
                        if (!listWithoutDuplicates.Contains(board[i][j])) //Checks row if duplicate.
                        {
                            listWithoutDuplicates.Add(board[i][j]);
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
                [['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
                ['6', '.', '.', '1', '9', '5', '.', '.', '.'], 
                ['.', '9', '8', '.', '.', '.', '.', '6', '.'], 
                ['8', '.', '.', '.', '6', '.', '.', '.', '3'], 
                ['4', '.', '.', '8', '.', '3', '.', '.', '1'], 
                ['7', '.', '.', '.', '2', '.', '.', '.', '6'], 
                ['.', '6', '.', '.', '.', '.', '2', '8', '.'], 
                ['.', '.', '.', '4', '1', '9', '.', '.', '5'], 
                ['.', '.', '.', '.', '8', '.', '.', '7', '9']];

            char[][] board2 =
                [['8', '3', '.', '.', '7', '.', '.', '.', '.'],
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
        }
    }
}
