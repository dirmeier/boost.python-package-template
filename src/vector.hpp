#ifndef BOOST_EXAMPLE_HPP
#define BOOST_EXAMPLE_HPP

##include <vector>

class vector
{
    std::vector<double> get()
    {
        std::vector<double> vec(10);
        return vec;
    }
}

#endif