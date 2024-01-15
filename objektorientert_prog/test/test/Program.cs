namespace test
{
    class Program
    {
        static void Main(string[] args)
        {
            int res = 0;
            Console.Write("Write a number: ");
            string inp1 = Console.ReadLine();

            int num1;
            int.TryParse(inp1, out num1);
            
            Console.Write("Chose a operation: ");
            string opera = Console.ReadLine();

            Console.Write("Write another number: ");
            string inp2 = Console.ReadLine();

            int num2;
            int.TryParse(inp2, out num2);

            if (opera == "+") 
            { 
            res = num1 + num2;
            }
            if (opera == "-") 
            {
            res = num1 - num2;
            }

            Console.WriteLine($"result: {res}");
            int[] ints = { 1, 2, 3 };
            Console.Write(ints.Length);
            Console.WriteLine(Cube(5));
            Console.WriteLine("Yo");
            Console.WriteLine(GetPow(2,3));
        }

        static int Cube (int num)
        {
            int result = num * num * num;
            return result;
        }
        static int GetPow(int num, int pownum) 
        {
            for (int i = 0; i < pownum; i++)
            {
                num *= num;
            }
            return num;
        }
    }
}
