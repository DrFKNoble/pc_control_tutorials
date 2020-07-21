cmake_minimum_required(VERSION 3.5)

project(client LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5Core)
find_package(Qt5Network)

add_executable(listing_1
  main.cpp
  client.h
  client.cpp
)
target_link_libraries(listing_1 Qt5::Core Qt5::Network)
