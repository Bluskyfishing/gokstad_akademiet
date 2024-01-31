using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Bow : Weapon
    {
        public override string Attack()
        {
            return $"Bow: 3 arrows get shot out!";
        }
        public override string Description()
        {
            return "Made with spider string, it is very durable!";
        }
    }
}