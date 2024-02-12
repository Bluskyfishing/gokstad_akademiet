using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ikea_abstract.Products
{
    internal abstract class Product
    {
        protected float price;
        protected string shelfnumber;
        protected string description;

        public Product(float price, string shelfnumber, string description)
        {
            this.price = price;
            this.shelfnumber = shelfnumber;
            this.description = description;
        }
        public abstract float Price();
        public abstract string GetShelf();
        public abstract string Description();
    }
}
