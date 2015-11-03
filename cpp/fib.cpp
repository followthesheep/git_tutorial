
#include <iostream>
#include <vector>

void func(std::vector<int> &seq)
{
	int i = 1;
	int in = 1;
	int temp;
	for (auto &s : seq)
	{
		s = i;
		temp = in + i;
		i = in;
		in = temp;	 
	}
}

int main()
{
	int i;
	std::cout << "enter number: " << std::endl;
	std::cin >> i;
	std::vector<int> vec(i);
	func(vec);
	for(auto s : vec)
	{
		std::cout << s << std::endl;
	}	
}

