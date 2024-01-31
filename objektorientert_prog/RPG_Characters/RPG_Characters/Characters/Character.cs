using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace RPG_Characters.Characters
{
    public class Character
    {
        public string name;
        public string description;
        private string weaponEquip;
        public Character(string name, string description, string weaponEquip = "No weapon")
        {
            this.name = name;
            this.description = description;
            WeaponEquip = weaponEquip;
        }
        public string WeaponEquip
        {
            get { return weaponEquip; } //read
            set { weaponEquip = value; } //write
        }
        public virtual string Attack()
        {
            return $"{name} attacks with their barehands!?!?";
        }
        public virtual string Description()
        {
            return description;
        }
    }
}