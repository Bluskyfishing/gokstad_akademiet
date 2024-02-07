using Ikea_abstract.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ikea_abstract.Products
{
    internal class CookingPot : Product, IKitchen
    {
        public CookingPot(float price, string shelfnumber, string description) : base(price, shelfnumber, description)
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
        public string Kitchen()
        {
            return "This fits in the Kitchen!";
        }
    }
}
