cmake_minimum_required(VERSION 3.20)
project(euler C)

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

file(GLOB_RECURSE SOURCES
        "${CMAKE_SOURCE_DIR}/c/level_*/*.c"
)

message(STATUS "SOURCES = ${SOURCES}")

foreach(src ${SOURCES})
    get_filename_component(name ${src} NAME_WE)

    add_executable(${name}
            ${src}
            ${CMAKE_SOURCE_DIR}/c/perf/perf.c
    )

    target_include_directories(${name} PRIVATE
            ${CMAKE_SOURCE_DIR}/c/perf
    )
endforeach()