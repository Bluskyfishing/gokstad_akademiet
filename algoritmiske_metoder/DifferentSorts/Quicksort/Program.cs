int[] theNumbers = { 15, 123, 157, 56, 4, 171, 188, 42, 219, 107, 139, 253, 91, 23, 8, 204, 72, 148, 234, 16 };

Console.WriteLine("Unsorted: ");
foreach (int num in theNumbers)
{
    Console.Write(" " + num);
}

int[] sortedNumbers = Quicksort(theNumbers);

Console.WriteLine("\nSorted: ");

foreach (int num in sortedNumbers)
{
    Console.Write(" " + num);
}

static int[] Quicksort(int[] input)
{
    if (input.Length <= 1) 
    {  
        return input; 
    }

    int pivot = input[0];

    int[] less = new int[input.Length];
    int less_count = 0;
    int[] great = new int[input.Length];
    int great_count = 0;


    for (int i = 1; i < input.Length; i++)
    {
        int num = input[i];

        if (num <= pivot)
        {
            less[less_count] = num;
            less_count++;
        }

        if (num > pivot)
        {
            great[great_count] = num;
            great_count++;
        }
    }

    // maybe shorten arrays?
    Array.Resize(ref less, less_count);
    Array.Resize(ref great, great_count);


    // - sorting the partitions independently
    less = Quicksort(less);
    great = Quicksort(great);

    int[] result = new int[input.Length];
    int pos = 0;

    for (int i = 0; i < less.Length; i++)
    {
        if (less[i] != 0)
        {
            result[pos] = less[i];
            pos++;
        }
    }

    result[pos] = pivot;
    pos++;

    for (int i = 0; i < great.Length; i++)
    {
        if (great[i] != 0)
        {
            result[pos] = great[i];
            pos++;
        }
    }

    return result;
}