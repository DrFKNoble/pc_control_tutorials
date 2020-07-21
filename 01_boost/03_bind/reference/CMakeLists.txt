cmake_minimum_required(VERSION 3.5)

project(main)

set(CMAKE_CXX_STANDARD 17)

set(BOOST_ROOT "C:/boost_1_73_0")
find_package(Boost)

include_directories(${Boost_INCLUDE_DIRS})
link_directories(${Boost_LIBRARIES_DIRS})

add_executable(main main.cpp)

target_link_libraries(main ${Boost_LIBRARIES})

# Utilities

# Build

# Install

install(TARGETS main DESTINATION ${PROJECT_SOURCE_DIR}/bin)