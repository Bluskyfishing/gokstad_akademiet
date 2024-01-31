using RPG_Characters.Characters;
using RPG_Characters.Weapons;
using System;

namespace RPG_Characters
{
    internal class Program
    {
        static void Main(string[] args)
        {
           Dagger dagger  = new Dagger();
           Rogue rogue1 = new Rogue("Nirith",
               "An experienced Rogue, killing enemies in the blink of an eye.",
               dagger.Attack());

           Console.WriteLine(rogue1.name);
           Console.WriteLine(rogue1.Attack());
           Console.WriteLine(rogue1.Description());

           //no item rouge
           Rogue rouge2 = new Rogue("Anjanath", "A very strong rogue, but doesnt like weapons.");
           Console.WriteLine(rouge2.name);
           Console.WriteLine(rouge2.Attack());
           Console.WriteLine(rouge2.Description());
        }
    }
}