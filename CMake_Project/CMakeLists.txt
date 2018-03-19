cmake_minimum_required(VERSION 3.8)
project(MIPT_TP_Homework_Sem)

set(CMAKE_CXX_STANDARD 11)

set(SOURCE_FILES B/main.cpp)
add_executable(CMakeProject ${SOURCE_FILES})

add_custom_target(script
        WORKING_DIRECTORY "${CMAKE_CURRENT_SOURCE_DIR}/A"
        COMMAND python ./script.py)

add_dependencies(CMakeProject script)

target_include_directories(CMakeProject PUBLIC "")
