using Ikea_abstract.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Reflection;
using System.Text;
using System.Threading.Tasks;

namespace Ikea_abstract.Products
{
    internal class Carpet : Product, ILivingRoom, IOffice, IBedroom
    {
        public Carpet(float price, string shelfnumber, string description) : base(price, shelfnumber, description) 
        { 
        }
        public override float Price()
        {
            return price;
        }
        public override string GetShelf()
        {
            return shelfnumber;
        }
        public override string Description()
        {
            return description;
        }
        public string LivingRoom()
        {
            return "This fits in the living room!";
        }
        public string Office()
        {
            return "This fits in the office!";
        }
        public string Bedroom()
        {
            return "This fits in the Bedroom()!";
        }
    }
}
