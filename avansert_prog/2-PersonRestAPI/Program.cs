using _2_PersonRestAPI.Models;
using System.Net.Cache;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

// making endpoint. Method: GET. ON: https://localhost:7251/persons
app.MapGet("/persons", () => 
{
    var person = new Person { Age = 20, id = 1, FirstName = "Ola", LastName = "Normann" };
    return Results.Ok(person);
}).WithName("Persons");

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

app.Run();