#include <iostream>
#include <vector>
#include <string>
//Takes a phrase like "turpentine and turtles" and translate it into its “whale talk” equivalent, "uueeieeauuee"
int main() {
  
  std::string input = "Turpentine and turtles.";

  std::vector<char> vowels;

  vowels.push_back('a');
  vowels.push_back('e');
  vowels.push_back('i');
  vowels.push_back('o');
  vowels.push_back('u');

  std::vector<char> whale_talk;

  for (int i = 0; i < input.size(); i++) {
    // nested loop!
    for (int j = 0; j < vowels.size(); j++) {

      if (input[i] == vowels[j]) {

        whale_talk.push_back(input[i]);
       
        if (input[i] == 'e' || input [i] == 'u') {

        whale_talk.push_back(input[i]);
        
        }
      
      }
      
    }
  
  }
  // Whales double the es and the us in their language.
  for (int k = 0; k < whale_talk.size(); k++) {
    
    std::cout << whale_talk[k];
    
  }
  
  std::cout << "\n";
  
}