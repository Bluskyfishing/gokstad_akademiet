using Ikea_abstract.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ikea_abstract.Products
{
    internal class BookShelf : Product, IAssemblable, ILivingRoom, IOffice, IBedroom
    {
        private string assemble;
        internal BookShelf(float price, string shelfnumber, string description, string assemble) : base(price, shelfnumber, description)
        {
            this.assemble = assemble;
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
        public string Assemble()
        {
            return assemble;
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