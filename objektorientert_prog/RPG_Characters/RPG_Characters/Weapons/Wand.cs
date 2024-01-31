using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Wand : Weapon
    {
        public override string Attack()
        {
            return $"Wand: sparkeling brightly";
        }
        public override string Description()
        {
            return "A little stick looking thing.";
        }
    }
}