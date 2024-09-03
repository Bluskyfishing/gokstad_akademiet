static int[] Sort(int[] input)
{
    for (int j = 0; j < input.Length; j++)
    {
        for (int i = 0; i < input.Length - 1; i++)
        {
            if (input[i] > input[i + 1])
            {
                // swap
                int temp = input[i + 1];
                input[i + 1] = input[i];
                input[i] = temp;
                continue;
            }
        }

    }
    
    return input;
}

static bool IsSorted(int[] input)
{
    for (int i = 0; i < input.Length - 1; i++)
    {
        if (input[i] > input[i + 1])
        {
            return false;
        }
    }
    return true;
}

int[] the_numbers = { 15, 123, 157, 56, 4, 171, 188, 42, 219, 107, 139, 253, 91, 23, 8, 204, 72, 148, 234, 16 };

// numbers print
foreach (int i in the_numbers)
{
    Console.Write(i + " ");
}

Console.WriteLine("\nIs sorted: " + IsSorted(the_numbers) + "\n");

// numbers sort print
int[] sortedNumbers = Sort(the_numbers);

foreach (int i in sortedNumbers)
{
    Console.Write(i + " ");
}

Console.WriteLine("\nIs sorted: " + IsSorted(sortedNumbers));