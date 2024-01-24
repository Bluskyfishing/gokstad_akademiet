using animal_Inheritance;
using System;
using System.Collections.Generic;

namespace animal_inheritance{
    internal class Program {
        static void Main(string[] args) {
            List<Pet> pets = new List<Pet>();

            pets.Add(new Dog("Bjarne"));
            pets.Add(new Dog("Bjarte"));
            pets.Add(new Cat("Kalle"));
            pets.Add(new Cat("Kristian"));
            pets.Add(new Fish("Oscar"));
            pets.Add(new Fish("Ole"));
            

            foreach (Pet pet in pets) {
                pet.GetName();
                pet.GetNoise();
                pet.GetTrick();
                Console.WriteLine();
            }
           
        }
    }
}