using System;
using System.Collections.Generic;
using System.ComponentModel.DataAnnotations;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace animal_Inheritance {

    public class Pet {
        public string name;
        public string noise;
        public string trick;
        public Pet(string name, string noise, string trick) {
            this.name = name;
            this.noise = noise;
            this.trick = trick;
        }

            public virtual void GetName() {
                Console.WriteLine("Pet Name: " + name);
            }
            public virtual void GetNoise() {
                Console.WriteLine("The animal makes a noise: " + noise);
            }
            public virtual void GetTrick() {
                Console.WriteLine("The animal does a trick: " + trick);
            }
    }
    public class Dog(string name) : Pet(name, "Woof", "*Fetches ball*") {
    
    }
    public class Cat(string name) : Pet(name, "Meow", "*sleeps*") {

    }
    public class Fish(string name) : Pet(name, "Blub", "*Jumps out of water*") {

    }
}
