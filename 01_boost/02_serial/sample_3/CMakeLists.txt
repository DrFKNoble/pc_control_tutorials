cmake_minimum_required(VERSION 3.5.1)

project(sample_3)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set (BOOST_ROOT "C:/boost_1_73_0")

find_package(Boost)

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

add_library(serial serial.cpp)

add_executable(sample_3 main.cpp)
target_link_libraries(sample_3 serial ${Boost_LIBRARIES})

# Utilities

set(CMAKE_DIR "C:/Program Files/CMake")
find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)

# Build

# Install

install(TARGETS sample_3 DESTINATION ${PROJECT_SOURCE_DIR}/bin)
