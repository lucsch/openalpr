cmake_minimum_required(VERSION 3.0)
project("openalpr")

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()

add_subdirectory(src)