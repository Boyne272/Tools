#include "menu.h";

// example from previous project
class test_menu : public menu {
public:
	// setup
	test_menu()
	{
			// note add /t to command name if it is short
		this->command_map["example"] = 0;
		this->desctriptions["example\t"] = string("This is a decription for a command");

			
		this->command_map["number"] = 1;
		this->desctriptions["number\t"] = string("A robust way to enter a number within optional limits");

		this->command_map["string"] = 2;
		this->desctriptions["string\t"] = string("Enter a string that is restricted in what it can and can't contain");

		this->command_map["options"] = 3;
		this->desctriptions["options\t"] = string("Enter any intput from a list of options");

		this->command_map["bool"] = 4;
		this->desctriptions["bool\t"] = string("Enter a boolian choice");

		this->intro = string("An example of a menu by Richard Boyne\n");
	}

	void commands(int opt) {
		switch (opt) {

			// here it is nice to describe what each option does
		case 0: {
			cout << " you entered command 1 \n the code could do something here";
			break;
		}


			// example of the enter_int function
		case 1: {
			cout << "enter an iteger between 0 and 10: ";
			int n = this->enter_int(0, 10);
			cout << "you entered " << n;
			break;
		}


			// example of the enter_string function
		case 2: {
			cout << "enter a name with an a but without an e: ";
			string s = this->enter_string("a", "e");
			cout << "you entered " << s;
			break;
		}
			

			// example of the enter_options function
		case 3: {
			cout << "what is your favourite chocolate (white, milk ot dark): ";
			string options[] = { "white", "milk", "dark" };
			string s = this->enter_options(options, 3);
			cout << "you like " << s << " chocolate";
			break;
		}
				

			// example of the enter_bool function
		case 4: {
			cout << "(y/n) do you like britney spears: ";
			bool c = this->enter_bool();
			if (c)
				cout << "Nice!";
			else
				cout << "Lame";
			break;
		}

		}
	}
};


int main() {
	test_menu().start();
}