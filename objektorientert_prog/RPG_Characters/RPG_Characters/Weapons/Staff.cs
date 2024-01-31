using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Staff : Weapon
    {
        public override string Attack()
        {
            return $"Staff: Starts to glow uncontrollably, why is it raining acid?";
        }
        public override string Description()
        {
            return "A scepter, looks like a king used this before?";
        }
    }
}