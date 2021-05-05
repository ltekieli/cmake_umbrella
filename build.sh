#!/bin/bash

set -euo pipefail

INSTALL_PREFIX=/tmp/umbrella
CMAKE_FLAGS=" \
    -DBUILD_SHARED_LIBS=ON \
    -DCMAKE_CXX_COMPILER_LAUNCHER=ccache \
    -DCMAKE_PREFIX_PATH="${INSTALL_PREFIX}\;${PWD}/build-conan" \
    -DCMAKE_MODULE_PATH=${PWD}/build-conan \
    -DCMAKE_INSTALL_RPATH=\$ORIGIN/../lib \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON"
JOBS=$(nproc)

function deps() {
    rm -rf build-conan
    mkdir build-conan
    pushd build-conan
    conan install ../
    conan imports ../ -imf ${INSTALL_PREFIX}
    popd
}

function single_library() {
    local target="$1"
    rm -rf "build-${target}" && mkdir "build-${target}"
    pushd "build-${target}"
    # shellcheck disable=SC2086
    cmake ../lib/"${target}" ${CMAKE_FLAGS}
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix "${INSTALL_PREFIX}"
    popd
}

function single_app() {
    local target="$1"
    rm -rf "build-${target}" && mkdir "build-${target}"
    pushd "build-${target}"
    # shellcheck disable=SC2086
    cmake ../apps/"${target}" ${CMAKE_FLAGS}
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix "${INSTALL_PREFIX}"
    popd
}

function build_separate() {
    rm -rf "${INSTALL_PREFIX}"
    deps
    single_library logging
    single_library rpc
    single_library abstract
    single_app worker
}

function build_together() {
    rm -rf "${INSTALL_PREFIX}"
    deps
    rm -rf build && mkdir build
    pushd build
    # shellcheck disable=SC2086
    cmake ../ ${CMAKE_FLAGS}
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix "${INSTALL_PREFIX}"
    popd
}

function test_units() {
    build_together
    pushd build
    ctest -V -j "${JOBS}"
    popd
}

function test_components() {
    build_together
    tox -- --install-prefix="${INSTALL_PREFIX}" -s
}

function build_all() {
    build_separate
    build_together
    test_units
    test_components
}

function clean() {
    rm -rf build
    rm -rf build-*
    rm -rf "${INSTALL_PREFIX}"
    rm -rf .tox
}

function help() {
    echo "./build.sh <function>"
    echo
    echo "Use one of the following functions:"
    echo "  build_all"
    echo "  build_separate"
    echo "  build_together"
    echo "  test_units"
    echo "  test_components"
    echo "  clean"
}

case ${1:-help} in
    build_all|build_separate|build_together|clean)
        $1
        ;;
    test_units|test_components)
        $1
        ;;
    *)
        help
        ;;
esac
