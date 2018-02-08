#ifndef BOOST_GRAPH_HPP
#define BOOST_GRAPH_HPP

#include <vector>
#include <boost/python.hpp>

class graph
{
public:
    graph(){};
    std::vector<double> get()
    {
        std::vector<double> vec(10);
        return vec;
    }
};


#endif