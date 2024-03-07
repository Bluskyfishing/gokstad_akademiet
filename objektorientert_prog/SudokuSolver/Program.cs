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
                bool result = false;
                bool charCheck = false;
                char[][] permutation;
                int counter = 1; 

                if (board.Length == 9)
                {
                    while (true)
                    {
                        counter++;
                        if (counter == 3)
                        {
                            break;
                        }
                        for (int i = 0; i < board.Length; i++)
                        {
                            Console.WriteLine(board[i]);
                            if (board[i].Length == 9) //first check list if so it doesnt have any repeating numbers.
                            {
                                for (int j = 0; j < board[i].Length; j++) //1-9 generator, checks if in array, and if number is in same index.
                                {
                                    Console.WriteLine(board[i][j]);
                                }

                            }
                        }
                    }

                }
                return result;
            }
        }
        static void Main(string[] args)
        {
            char[][] board = 
                [['5', '3', '.', '.', '7', '.', '.', '.', '7'], 
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
        }
    }
}
