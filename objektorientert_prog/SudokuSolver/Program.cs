using System;
using System.Linq;
namespace SudokuSolver
{
    internal class Program
    {
        public class Solution
        {
            public bool IsValidSudoku(char[][] board)
            {
                if (board.Length == 9 )
                {
                    for ( int i = 0; i < board.Length; i++ )
                    {
                        if (board[i].Length == 9 )
                        {
                            for (int j = 0; j < board[i].Length; j++) 
                            {                                         
                                if (Char.IsDigit(board[i][j]) || board[i][j] == '.')
                                {
                                    if (Array.IndexOf(board[i], board[i][j]) >= 0) //check if number is in row.(vertical)
                                    {
                                        return false;
                                    }
                                    if (Array.IndexOf(board[j], board[j][i]) >= 0) //check if number is in column. (horizontal)
                                    {
                                        return false;
                                    } 
                                }

                            }
                        }
                    }
                }
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
