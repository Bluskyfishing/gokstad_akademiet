using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Weapon
    {
        public virtual string Attack()
        {
            return $"The weapon does the thing! *attacks*";
        }
        public virtual string Description()
        {
            return "This is like a weapon where you like attack and stuff...";
        }
    }
}