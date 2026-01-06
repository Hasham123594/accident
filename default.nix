{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    git
    python312
    uv

    # runtime libs commonly needed by numpy/pandas wheels
    zlib
    stdenv.cc.cc.lib
  ];

  shellHook = ''
    export LD_LIBRARY_PATH="${pkgs.lib.makeLibraryPath (with pkgs; [ zlib stdenv.cc.cc.lib ])}:$LD_LIBRARY_PATH"
  '';
}
