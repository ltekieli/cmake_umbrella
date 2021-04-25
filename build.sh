#!/bin/bash

set -euo pipefail

INSTALL_PREFIX=/tmp/umbrella
CMAKE_FLAGS="-DBUILD_SHARED_LIBS=OFF -DCMAKE_CXX_COMPILER_LAUNCHER=ccache -DCMAKE_PREFIX_PATH=${INSTALL_PREFIX}"
JOBS=$(nproc)

function single_library() {
    local target="$1"
    rm -rf "build-${target}" && mkdir "build-${target}"
    pushd "build-${target}"
    cmake ../lib/"${target}" ${CMAKE_FLAGS}
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix="${INSTALL_PREFIX}"
    popd
}

function single_app() {
    local target="$1"
    rm -rf "build-${target}" && mkdir "build-${target}"
    pushd "build-${target}"
    cmake ../apps/"${target}" ${CMAKE_FLAGS}
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix="${INSTALL_PREFIX}"
    popd
}

function build_separate() {
    rm -rf "${INSTALL_PREFIX}"
    single_library logging
    single_library rpc
    single_library abstract
    single_app worker
}

function build_together() {
    rm -rf "${INSTALL_PREFIX}"
    rm -rf build && mkdir build
    pushd build
    cmake ../
    cmake --build . --target all --parallel "${JOBS}"
    cmake --install . --prefix="${INSTALL_PREFIX}"
    popd
}

function clean() {
    rm -rf build
    rm -rf build-*
    rm -rf "${INSTALL_PREFIX}"
}

if [ $# -eq 0 ]; then
    echo "Sepcify build_separate or build_together"
else
    "$1"
fi
