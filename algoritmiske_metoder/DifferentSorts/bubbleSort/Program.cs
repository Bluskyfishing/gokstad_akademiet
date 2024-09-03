using bubbleSort;

int[] sort(int[] input)
{
    for (int i = 0; i < input.Length; i++)
    {
        for (int j = i; j < input.Length; j++)
        {
            if (input[i] > input[j])
            {
                int temp = input[i];
                input[i] = input[j];
                input[j] = temp;
            }
        }
    }
    return input;
}

int[] theNumbers = { 15, 123, 157, 56, 4, 171, 188, 42, 219, 107, 139, 253, 91, 23, 8, 204, 72, 148, 234, 16 };

Console.WriteLine("Unsorted: " + sortUtils.isSorted(theNumbers));
foreach (int i in theNumbers)
{
    Console.Write(i + " ");
}

int[] sortedNumbers = sort(theNumbers);
Console.WriteLine("\n\nSorted: " + sortUtils.isSorted(sortedNumbers));
foreach (int i in sortedNumbers)
{
    Console.Write(i + " ");
}