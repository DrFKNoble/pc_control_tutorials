cmake_minimum_required(VERSION 3.5.1)

project(activity_2)

find_package(Boost 1.70.0 REQUIRED)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

include_directories(${Boost_INCLUDE_DIR})
link_directories(${Boost_LIBRARY_DIRS})

add_executable(activity_2 main.cpp)
target_link_libraries(activity_2 ${Boost_LIBRARIES})

# Utilities

set(CMAKE_DIR "C:/Program Files/CMake")
find_program(CMAKE_EXECUTABLE NAMES cmake HINTS ${CMAKE_DIR} ENV CMAKE_DIR PATH_SUFFIXES bin)

# Build

# Install

install(TARGETS activity_2 DESTINATION ${PROJECT_SOURCE_DIR}/bin)