using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace recursiveList
{
    public class Node
    {
        public string item_value { get; set; }
        public Node next { get; set; }

        public Node(string item_value)
        {
            this.item_value = item_value;
            this.next = null;
        }
    }

    public class LinkedList
    {
        public Node head;

        public LinkedList()
        {
            this.head = null;
        }

        public void addMethod(string input)
        {
            if (this.head == null)
            {
                this.head = new Node(input);
            }
            else
            {
                Node tail = addRecursive(this.head);
                tail.next = new Node(input);
            }

        }
        public Node addRecursive(Node node) 
        {
            if (node.next == null) { return node; }

            Node tail = addRecursive(node.next);
            return tail;
        }

        public bool removeMethod(string input)
        {

            removeMethod(input);
            return false;
        }

        public bool findMethod(string input)
        {

            //findMethod();

            return false;
        }

        public void nodeListPrint(Node node)
        {
            if (node == null ) {return;}

            Console.WriteLine(node.item_value);
            nodeListPrint(node.next);
        }
    }
}