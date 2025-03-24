#include <iostream>
#include <string>

using namespace std;

void showHelp() {
    cout << "🔹 Kiddo01 Runtime Help:\n";
    cout << "run <file.kiddo> - Kör en Kiddo01 fil\n";
    cout << "help - Visar hjälpmeddelande\n";
}

void runFile(const std::string& filename) {
    if (filename == "test.kiddo") {
        cout << "Hello Kiddo!" << endl;
    } else {
        cout << "⚠️ Filen hittades inte." << endl;
    }
}

int main(int argc, char* argv[]) {
    if (argc < 2) {
        cout << "⚠️ No command provided. Använd 'help' för hjälp.\n";
        return 1;
    }

    string command = argv[1];

    if (command == "help") {
        showHelp();
    } else if (command == "run") {
        if (argc < 3) {
            cout << "⚠️ Please provide a filename to run." << endl;
        } else {
            runFile(argv[2]);
        }
    } else {
        cout << "⚠️ Unknown command: " << command << ". Använd 'help'." << endl;
    }

    return 0;
}
