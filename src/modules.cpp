#include <boost/python.hpp>
#include "vector.hpp"

boost::python::BOOST_PYTHON_MODULE(modules)
{
    boost::python::class_<vector>("vector")
        .def("get", &vector::get);
}
