using System;

namespace Calc
{
    internal class Program
    {
        static void CalcMethod(float num, float num2, string mathOperator)
        {
            float result;
            switch (mathOperator)
            {
                case "+":
                    result = num + num2;
                    Console.WriteLine($"{num} {mathOperator} {num2} = {result}");
                    break;
                case "-":
                    result = num - num2;
                    Console.WriteLine($"{num} {mathOperator} {num2} = {result}");
                    break;
                case "*":
                    result = num * num2;
                    Console.WriteLine($"{num} {mathOperator} {num2} = {result}");
                    break;
                case "/":
                    result = num - num2;
                    if (num2 == 0.0)
                    {
                        Console.WriteLine("Cant divde by 0!");
                        break;
                    }
                    Console.WriteLine($"{num} {mathOperator} {num2} = {result}");
                    break;
                default:
                    Console.WriteLine("Unknown mathoperator Try again!");
                    break;

            }
        }

        static void Main(string[] args)
        {
            while (true)
            {
                Console.WriteLine("Write 'exit' to exit!");
                Console.WriteLine("Write a number:");
                string input = Console.ReadLine();

                if (float.TryParse(input, out float num1))
                {
                    Console.WriteLine("Write a second number:");
                    string input2 = Console.ReadLine();

                    if (float.TryParse(input2, out float num2))
                    {
                        Console.WriteLine("Write a operator number:");
                        string mathOperator = Console.ReadLine();

                        CalcMethod(num1, num2, mathOperator);
                    }
                    else
                    {
                        Console.WriteLine("Input has to be a number! 2");
                    }
                }
                else if (input == "exit")
                {
                    break;
                }
                else
                {
                    Console.WriteLine("Input has to be a number! 1");
                }
            }
        }
    }
}