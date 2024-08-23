using recursiveList;

LinkedList linkedList = new LinkedList();

// add method 
Console.WriteLine("add method:");
linkedList.addMethod("hei");
linkedList.addMethod("på");
linkedList.addMethod("deg");
linkedList.addMethod("deg"); // Try to add duplicate
linkedList.addMethod("!");

linkedList.nodeListPrint(linkedList.head);

// find method 
Console.WriteLine("\nfind method: ");
Console.WriteLine("Find 'deg' in linkedList: " + linkedList.findMethod(linkedList.head, "deg").item_value);

// item not in list.
// linkedList.findMethod(linkedList.head, "degX"); // NULL

// remove method 
Console.WriteLine("\nremove method (hei, deg): ");
linkedList.removeMethod(linkedList.head, "hei");
linkedList.removeMethod(linkedList.head, "deg");

linkedList.nodeListPrint(linkedList.head);

//Fibonacci.fib(0,1, 100);