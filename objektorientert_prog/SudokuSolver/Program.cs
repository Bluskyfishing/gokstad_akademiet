namespace SudokuSolver
{
    internal class Program
    {
        public class Solution
        {
            public bool IsValidSudoku(char[][] board)
            {
                bool result = false;
                char[][] permutation;

                if (board.Length == 9)
                {
                    while (true)
                    {
                        if () 
                        {
                            break;
                        } //What should be the exit? 
                        for (int i = 0; i < board.Length; i++)
                        {
                            Console.WriteLine(board[i]);
                            if (board[i].Length == 9) //first check list if so it doesnt have any repeating numbers.
                            {
                                for (int j = 0; j < board[i].Length; j++)
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
                [['5', '3', '.', '.', '7', '.', '.', '.', '.'], 
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
