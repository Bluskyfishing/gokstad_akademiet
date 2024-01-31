using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Characters
{
    public class Rogue : Character
    {
        public Rogue(string name, string description, string WeaponEquip = "No weapon") : base(name, description, WeaponEquip)
        {
        }
        public override string Attack()
        {
            if (WeaponEquip != "No weapon") //Accesses the get property
                return WeaponEquip; //returns string in argument

            return $"{name} goes invis and stabs in the back!";
        }
    }
}