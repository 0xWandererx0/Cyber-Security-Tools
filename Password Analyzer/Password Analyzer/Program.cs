using System;

class Program
{
    static void Main()
    {

        Console.Write("Kaç adet şifre analizi yapacaksınız?: ");
        int adet = Convert.ToInt32(Console.ReadLine()); 
        
        string[] sifreler = new string[adet];

        for (int i = 0; i < adet; i++)
        {
            Console.Write((i + 1) + "Lütfen şifrenizi giriniz: ");
            sifreler[i] = Console.ReadLine();
        }

        Console.WriteLine("\n--- ANALİZ BAŞLIYOR ---\n");

        for (int i = 0; i < sifreler.Length; i++)
        {
            if (sifreler[i].Length < 8)
            {
                Console.ForegroundColor = ConsoleColor.Red;
                Console.WriteLine("ZAYIF: " + sifreler[i] + " (Çok kısa!)");

            }

            else
            {
                Console.ForegroundColor = ConsoleColor.Green;
                Console.WriteLine("GÜÇLÜ: " + sifreler[i] + " (Yeterli uzunlukta!)");

            }
        }
        Console.ResetColor();
        Console.Read();




    }
}
