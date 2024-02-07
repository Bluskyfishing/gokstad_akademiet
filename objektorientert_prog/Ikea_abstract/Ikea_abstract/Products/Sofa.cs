using Ikea_abstract.Interfaces;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ikea_abstract.Products
{
    internal class Sofa : Product, IAssemblable, ILivingRoom
    {
        private string assemble;
        internal Sofa(float price, string shelfnumber, string description, string assemble) : base(price, shelfnumber, description)
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
    }
}