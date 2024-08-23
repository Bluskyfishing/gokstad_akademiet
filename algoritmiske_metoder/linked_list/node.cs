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
            if (findMethod(this.head, input) !=  null) 
            {
                Console.WriteLine("Cannot add duplicate element!");
                return;    
            }

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
        public Node findMethod(Node node, string input)
        {
            if (node == null) { return null; }
            if (node.item_value == input) { return node; }

            Node found = findMethod(node.next, input);

            return found;
        }

        public Node removeMethod(Node node,  string input)
        {
            if (node == null) { return node; }

            if (node.item_value == input) 
            {
                if (node == this.head)
                {
                    return this.head = node.next;
                }
                return node.next;
            }

            node.next = removeMethod(node.next, input);

            return node;
        }

        public void nodeListPrint(Node node)
        {
            if (node == null ) {return;}

            Console.WriteLine(node.item_value);
            nodeListPrint(node.next);
        }
    }
}