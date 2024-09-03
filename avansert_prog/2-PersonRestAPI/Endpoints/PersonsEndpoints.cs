using _2_PersonRestAPI.Models;
using System.Reflection.Metadata.Ecma335;
using System.Runtime.CompilerServices;

namespace _2_PersonRestAPI.Endpoints
{
    public static class PersonsEndpoints
    {
        public static void MapPersonEndpoints(this WebApplication app)
        {
            app.MapGet("/persons", GetPersons), 
                Person person => return Results.Ok(new Person() LastName = person.LastName,id = person.id});
        }).WithName("AddPersons");

            app.MapPost("/persons", (Person person) =>
            {
                return Results.Ok(new Person()
                {
                    Age = person.Age + 1,
                    FirstName = person.FirstName,
                    LastName = person.LastName,
                    id = person.id

                });
            }).WithName("addPersons");
        }

        private static IResult GetPersons()
        {
            var person = new Person { Age = 20, id = 1, FirstName = "Ola", LastName = "Normann" };
            return Results.Ok(person);
        }
        private static IResult Addperson(Person person)
        {

        }
        
    }
}
