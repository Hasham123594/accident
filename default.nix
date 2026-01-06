{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  packages = with pkgs; [
    git
    python312
    uv
    stdenv.cc.cc.lib
  ];
}
