using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Characters
{
    public class Wizard : Character
    {
        public Wizard(string name, string description, string WeaponEquip = "No weapon") : base(name, description, WeaponEquip)
        {
        }
        public override string Attack()
        {
            if (WeaponEquip != "No weapon") 
                return WeaponEquip; 

            return $"{name} Casts giga fireball!";
        }
    }
}