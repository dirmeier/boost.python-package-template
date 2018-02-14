
#include <boost/python.hpp>
#include "graph.hpp"

using namespace boost::python;
BOOST_PYTHON_MODULE(boostmodules)
{
    class_<graph>("graph", init<>())
        .def("get", &graph::get);
}
