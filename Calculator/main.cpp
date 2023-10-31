#include <iostream>
#include <iomanip>
#include <string>
#include <cmath>
#include <cctype>
using namespace std;
// prototype menu
void display_menu();
char get_selection();
void handle_quit();
void handle_unknown();
// prototype math functions
void add_num(double);
void sub_num(double);
void multiply(double);
void divide(double);
void permiter(double);

int main()
{
    char selection{};
    double total{};
    do
    {
        display_menu();
        selection = get_selection();
        switch (selection)
        {
        case 'A':
            add_num(total);
            break;
        case 'S':
            sub_num(total);
            break;
        case 'M':
            multiply(total);
            break;
        case 'D':
            divide(total);
            break;    
        case 'Q':
            handle_quit();
            break;
        default:
            handle_unknown();
        }
    } while (selection != 'Q');
    cout << endl;
    return 0;
}

void display_menu()
{
    cout << "\nIan's Math Calculator \n";
    cout << "A - Add numbers \n";
    cout << "S - Subtract number \n";
    cout << "D - Divide\n";
    cout << "M - Multiply\n";
    cout << "Q - Quit \n";
    cout << "\nEnter your choice: ";
}
char get_selection()
{
    char choice{};
    cin >> choice;
    return toupper(choice);
}
void handle_quit()
{
    cout << "Goodbye" << endl;
}
void handle_unknown()
{
    cout << "Unknown selection - try again" << endl;
}
void add_num(double)
{
    double a{}, b{}, total{};
    cout << "Enter 2 numbers ";
    while (true) {
        if (cin >> a >> b){
            total = a + b;
            cout << "= " << total << endl;
            break;
    }   else {
            cout << "Try agin! Enter a valid integer value!\n";
            cin.clear();
        }
    }
}
void sub_num(double)
{
    double a{}, b{}, total{};
    cout << "Enter 2 numbers ";
    while (true) {
        if (cin >> a >> b){
            total = a - b;
            cout << "= " << total << endl;
            break;
    }   else {
            cout << "Try agin! Enter a valid integer value!\n";
            cin.clear();
        }
    }
}
void multiply(double)
{
    double a{}, b{}, total{};
    cout << "Enter 2 numbers ";
    while (true) {
        if (cin >> a >> b){
            total = a * b;
            cout << "= " << total << endl;
            break;
    }   else {
            cout << "Try agin! Enter a valid integer value!\n";
            cin.clear();
        }
    }
}
void divide(double)
{
    double a{}, b{}, total{};
    cout << "Enter 2 numbers ";
    while (true) {
        if (cin >> a >> b){
            total = a / b;
            cout << "= " << total << endl;
            break;
    }   else {
            cout << "Try agin! Enter a valid integer value!\n";
            cin.clear();
        }
    } 
}