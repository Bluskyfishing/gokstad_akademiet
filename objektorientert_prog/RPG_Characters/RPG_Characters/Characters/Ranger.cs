using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Characters
{
    public class Ranger : Character
    {
        public Ranger(string name, string description, string WeaponEquip = "No weapon") : base(name, description, WeaponEquip)
        {
        }
        public override string Attack()
        {
            if (WeaponEquip != "No weapon")
                return WeaponEquip;

            return $"{name} shoots a big arrow!";
        }
    }
}