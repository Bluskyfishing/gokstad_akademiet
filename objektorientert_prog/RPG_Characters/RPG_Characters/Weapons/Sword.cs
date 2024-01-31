using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Sword : Weapon
    {
        public override string Attack()
        {
            return $"Sword: the sword throws itself!";
        }
        public override string Description()
        {
            return "A treesword, just made by a kid.";
        }
    }
}