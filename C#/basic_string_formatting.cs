/* Perform Basic String Formatting in C# */

string name = "John";
string name2 = " Peter";

Console.WriteLine(name + name2);

string firstname = "João Gabriel";
string lastname = "Savioli";
string message = firstname + " " + lastname + " is ok";

Console.WriteLine(message);

string nameb = "Bob";
string msg = $"Hello {nameb}";
Console.WriteLine(msg);

int winver = 11;
string msgwin = "Update Windows";
string final = $"{msgwin} {winver} ";
Console.WriteLine(final);

Console.WriteLine("\nAplicação Geral\n");

Console.WriteLine("Toyota Boshoku Services\n");

Console.WriteLine("Loading Services ...\n");

Console.WriteLine("Package 1: \t Complete");
Console.WriteLine("Package 2: \t Complete");
Console.WriteLine("Package 3: \t Incomplete");

Console.WriteLine("\nThere is something missing in the actual package! \n");
Console.WriteLine(@"!Notify!
Error in: \source\packages\sockets\dathfiles");

string solution = "Already done and fixed";
string status = "OK";

Console.WriteLine($"\nStatus: {solution}");
Console.WriteLine($"Project's status: {status}");

bool can = true;

Console.WriteLine($"\nThe project can continue. Server's response: {can} ");

Console.WriteLine("\nPackage 3 left in: \\source\\packages\\sockets\\dathfiles ");

var package3 = 3;

Console.WriteLine($"\nActual Package to be fixed: {package3}\n");

Console.WriteLine(@"source repo: \source\packages\sockets\dathfiles --->
GET Res:OK ; Err: BAD-PACKAGE ");
Console.WriteLine($"The package {package3} is OK ");

Console.WriteLine("\ninfo: All the packages were fixed ");


