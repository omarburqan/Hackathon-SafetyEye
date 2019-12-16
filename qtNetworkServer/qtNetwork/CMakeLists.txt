cmake_minimum_required(VERSION 3.5)

project(qtNetwork LANGUAGES CXX)

set(CMAKE_INCLUDE_CURRENT_DIR ON)

set(CMAKE_AUTOUIC ON)
set(CMAKE_AUTOMOC ON)
set(CMAKE_AUTORCC ON)

set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt5Core)
find_package(Qt5Network)
find_package(Qt5Gui)
find_package(OpenCV) 

add_executable(qtNetwork worker.h worker.cpp main.cpp)
target_link_libraries(qtNetwork Qt5::Core Qt5::Network Qt5::Gui ${OpenCV_LIBS})
