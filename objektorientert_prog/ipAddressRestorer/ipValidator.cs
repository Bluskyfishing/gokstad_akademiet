using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ipAddressRestorer
{
    public static class IPValidatorClass
    {
        public static string[] isIPValid(string[] IP)
        {
            string parts = IP.Split(",");
            Console.WriteLine(parts);
            return parts;
        }
    }
}
