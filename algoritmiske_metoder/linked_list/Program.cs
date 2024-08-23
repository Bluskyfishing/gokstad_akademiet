using recursiveList;

LinkedList linkedList = new LinkedList();

linkedList.addMethod("Hei");
linkedList.addMethod("på");
linkedList.addMethod("deg");
linkedList.addMethod("!");

linkedList.nodeListPrint(linkedList.head);

Console.WriteLine(linkedList.findMethod(linkedList.head, "deg"));

Console.WriteLine(linkedList.findMethod(linkedList.head, "degX")); // NULL 




//Fibonacci.fib(0,1, 100);