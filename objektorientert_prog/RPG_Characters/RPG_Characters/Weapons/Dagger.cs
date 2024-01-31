using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Weapons
{
    public class Dagger : Weapon
    {
        public override string Attack()
        {
            return $"Dagger: pokey poke attack!";
        }
        public override string Description()
        {
            return "2 butterknife, they requre alot of stabs...";
        }
    }
}